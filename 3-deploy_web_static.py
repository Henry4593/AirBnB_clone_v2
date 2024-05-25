#!/usr/bin/python3
"""Fabric script for streamlined web application deployment.

**Execution:**
fab -f 3-deploy_web_static.py deploy -i ~/.ssh/school -u ubuntu

This command leverages Fabric to execute the `deploy` function for streamlined
deployment.
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['54.237.217.113', '100.26.171.135']


def do_pack():
    """generates a tgz archive"""
    try:
        dt_time = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(dt_time)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """distributes archived files to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        file_no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, file_no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, file_no_ext))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, file_no_ext))
        run('rm -rf {}{}/web_static'.format(path, file_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, file_no_ext))
        return True
    except:
        return False


def deploy():
    """Orchestrates web application deployment process.
    1. Generates a compressed archive of the web application files.
    2. If archive creation fails, exits the function.
    3. Distributes the generated archive to the web servers.
    4. Returns True on successful deployment, False otherwise.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
