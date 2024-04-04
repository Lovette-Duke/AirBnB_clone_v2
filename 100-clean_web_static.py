#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
"""

from os.path import isdir, exists
from fabric.api import *
from datetime import datetime
env.hosts = ['35.174.211.179', '52.3.246.136']


def do_pack():
    """
    archiving the web_static folder
    """

    t = datetime.now()
    arch = 'web_static_' + t.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    archive = local('tar -cvzf versions/{} web_static'.format(arch))
    if archive is None:
        return None
    return arch


def do_deploy(archive_path):
    """distributes archive to web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_num = archive_path.split("/")[-1]
        split_f = file_num.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, split_f))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_num, path, split_f))
        run('rm /tmp/{}'.format(file_num))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, split_f))
        run('rm -rf {}{}/web_static'.format(path, split_f))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, split_f))
        return True
    except Exception:
        return False


def deploy():
    """calls the functions to create and distribute archives to web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


def do_clean(number=0):
    '''Clean webservers'''
    __path = 'versions/*.tgz'
    __exe = '/data/web_static/releases/web_static*'
    if number == 0:
        number = 1
    local("rm -f `ls -t {} | awk 'NR>{}'`".format(__path, number))
    run("rm -rf `ls -td {} | awk 'NR>{}'`".format(__exe, number))
