#!/usr/bin/python3
"""
distributes an archive to the different web servers
"""

from os.path import exists
from fabric.api import *
env.hosts = ['35.174.211.179', '52.3.246.136']


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
