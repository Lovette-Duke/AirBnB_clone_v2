#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
"""

from os.path import isdir, exists
from fabric.api import *
env.hosts = ['35.174.211.179', '52.3.246.136']


def do_clean(number=0):
    '''Deletes archives'''
    number = 1 if int(number) == 0 else int(number)

    # Delete local archives
    with lcd("versions"):
        local_archives = sorted(os.listdir("."))
        archives_to_delete = local_archives[:-number]
        for archive in archives_to_delete:
            local("rm ./{}".format(archive))
