"""config.py

Configuration file for pysync.py

"""

# Local path to pysynchelper.py script
LOCAL_PYSYNCHELPER_PATH = "/Users/ebelizar/pysync/"

# Local repository paths
LOCAL_PATH = {
    'admin': '/Users/ebelizar/gerrit_repos/wtinvadmin/',
    'tools': '/Users/ebelizar/gerrit_repos/wtinvtools/'
}

# DO NOT MODIFY CODE BELOW THIS LINE #

# Remote paths on server
REMOTE_PATH = {
    'admin': '/var/www/html/',
    'tools': '/usr/local/tools/invicta/'
}

# Python path
REMOTE_PYTHON_PATH = "/usr/local/bin/python2.7"

# SYNC_EXCLUDES is a list of files to exclude in the rsync
SYNC_EXCLUDES = [".git", "*.pyc", ".py", ".DS_Store", ".buildpath",
                 ".gitignore", ".project", ".settings"]

# rsync options
RSYNC_OPTIONS = 'rlpS'