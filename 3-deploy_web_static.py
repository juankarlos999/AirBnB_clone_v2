#!/usr/bin/python3
""" Automate the service on the server """
import os.path
from datetime import datetime
from fabric.api import *

env.hosts = ['35.237.186.94', '35.229.112.48']


def do_pack():
    """
    generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone
    repo, using the function do_pack
    """
    file_name = datetime.now().strftime("versions/web_static_%Y%m%d%H%M%S.tgz")
    print("Packing web_static to {}".format(file_name))
    try:
        with hide('output', 'running', 'warnings'):
            local('mkdir -p versions')
        local("tar -czvf {} web_static".format(file_name))
        with hide('output', 'running', 'warnings'):
            size_bytes = local("wc -c {}".format(file_name), capture=True)
        bytes_ = size_bytes.split()
        print("web_static packed: {} -> {}Bytes".format(file_name, bytes_[0]))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """
    Fabric script that distributes an archive to a web servers
    """
    if not os.path.exists(archive_path):
        return False

    file_tgz = archive_path.split('/')
    file_name = file_tgz[1].split('.')

    put(archive_path, '/tmp/{}'.format(file_tgz[1]))
    run('mkdir -p /data/web_static/releases/{}/'.format(file_name[0]))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'
        .format(file_tgz[1], file_name[0]))
    run('rm /tmp/{}'.format(file_tgz[1]))
    run('mv /data/web_static/releases/{}/web_static/*\
    /data/web_static/releases/{}/'.format(file_name[0], file_name[0]))
    run('rm -rf /data/web_static/releases/{}/web_static'
        .format(file_name[0]))
    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/{}/ \
        /data/web_static/current'.format(file_name[0]))
    print('New version deployed!')
    return True


def deploy():
    """
    Fabric script that creates and distributes an archive to a web server
    """
    file_path = do_pack()

    if not file_path:
        return False

    return do_deploy(archive_path)
