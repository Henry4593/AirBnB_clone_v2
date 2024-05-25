#!/usr/bin/python3
"""Fabric script for streamlined web application deployment.

**Execution:**
fab -f 3-deploy_web_static.py deploy -i ~/.ssh/school -u ubuntu

This command leverages Fabric to execute the `deploy` function for streamlined
deployment.
"""
import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once


env.hosts = ['54.237.217.113', '100.26.171.135']


@runs_once
def do_pack():
    """generates a tgz archive"""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    cur_time = datetime.now().strftime("%Y%m%d%H%M%S")
    output = "versions/web_static_{}.tgz".format(cur_time)
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        archize_size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, archize_size))
    except Exception:
        output = None
    return output


def do_deploy(archive_path):
    """distributes archived files to the web servers
    Args:
        archive_path (str): The path to the archived static files.
    """
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success


def deploy():
    """Orchestrates web application deployment process.
    1. Generates a compressed archive of the web application files.
    2. If archive creation fails, exits the function.
    3. Distributes the generated archive to the web servers.
    4. Returns True on successful deployment, False otherwise.
    """
    archive_path = do_pack()
    return do_deploy(archive_path) if archive_path else False
