#!/usr/bin/python3
"""
This script automates the deletion of excess archive files on remote servers.

It leverages Fabric to connect to the specified servers and cleans up archives
in two locations: versions directory and /data/web_static/releases directory.

You can control the number of archives to retain using the 'number' argument
when executing the script with Fab. For example:

fab -f 100-clean_web_static.py do_clean:number=2

- number=0 or 1: Keeps only the most recent archive.
- number=2: Keeps the most recent and second-most recent archives, and so on.
"""
import os
from fabric.api import *

env.hosts = ['54.237.217.113', '100.26.171.135']


def do_clean(number=0):
    """Deletes out-of-date archives on remote servers.

    Args:
        number (int, optional): The number of archives to keep. Defaults to 0.
            - 0 or 1: Keeps only the most recent archive.
            - 2: Keeps the most recent and second-most recent archives, and
            so on.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(archive)) for archive in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [archive for archive in archives if "web_static_" in
                    archive]
        [archives.pop() for _ in range(number)]
        [run("rm -rf ./{}".format(archive)) for archive in archives]
