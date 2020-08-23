#!/usr/bin/python3
""" Automate the service on the server """
from datetime import datetime
from fabric.api import *


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
