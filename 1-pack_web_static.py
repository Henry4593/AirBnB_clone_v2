#!/usr/bin/python3
"""This script generates a timestamped tar.gz archive of the 'web_static'
directory.

**Execution:**
fab -f 1-pack_web_static.py do_pack
This command uses Fabric to execute the `do_pack` function defined in this
script.
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """Creates a compressed archive (tar.gz) of the 'web_static' directory.
    The archive filename incorporates a timestamp for easy identification
    and is placed in a subdirectory named 'versions'.

    **Returns:**

    - The filename of the created archive (string) on success.
    - None if an error occurs during archive creation.
    """
    time = datetime.now()
    time_format = time.strftime("%Y%m%d%H%M%S")
    archive = "web_static_{}.tgz".format(time_format)
    local('mkdir -p versions')
    create_archive = local('tar -cvzf versions/{} web_static'.format(archive))
    if create_archive is not None:
        return archive
    else:
        return None
