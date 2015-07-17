#!/usr/bin/python2.7
"""pysync.py

A tool that will scp codebase files to remote server

"""

from Syncfiles import Syncfiles


def main():
    Syncfiles.outmsg("Starting pysync")

    # Get args
    args = Syncfiles.get_args()

    # Pass args into Syncfiles object
    syncfiles = Syncfiles(**vars(args))

    #TODO: Include db migrations logic

    # Sync files to the server(s)
    syncfiles.sync_files_to_server()

    Syncfiles.outmsg("Done.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        Syncfiles.outmsg("Error: {e}".format(e.message))
