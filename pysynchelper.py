"""pysynchelper.py

A helper script that will copy files from SSRA to partner/SSNs

This file will be stored in /tmp

"""

import argparse
import subprocess
import shlex


def get_list_of_commands(code_base, hostnames):
    cmds = []
    outmsg('Hostnames to sync: {h}'.format(h=hostnames))
    for hostname in hostnames.split(','):
        if code_base == "tools":
            path = '/usr/local/tools/invicta'
            cmds.append('scp -q -r {p}/ root@{h}:/usr/local/tools/'.format(p=path, h=hostname))
            cmds.append('scp -q {p}/checkhealth.sh root@{h}:/usr/local/tools/invicta/'.format(p=path, h=hostname))
            cmds.append('scp -q {p}/managedrives.sh root@{h}:/usr/local/tools/invicta/'.format(p=path, h=hostname))
            cmds.append('scp -q -r {p}/getslot/ root@{h}:/usr/local/tools/invicta/.'.format(p=path, h=hostname))
            cmds.append('scp -q -r {p}/sysUtils/ root@{h}:/usr/local/tools/invicta/.'.format(p=path, h=hostname))
            cmds.append('scp -q -r {p}/btl2/ root@{h}:/usr/local/tools/invicta/.'.format(p=path, h=hostname))
            cmds.append('scp -q -r {p}/ssb/ root@{h}:/usr/local/tools/invicta/.'.format(p=path, h=hostname))
            cmds.append('scp -q -r {p}/libpy/ root@{h}:/usr/local/tools/invicta/.'.format(p=path, h=hostname))
            cmds.append('scp -q -r {p}/scst/ root@{h}:/usr/local/tools/invicta/.'.format(p=path, h=hostname))
        elif code_base == "admin":
            path = '/var/www/html'
            cmds.append('rsync -rlpS --del {p}/ root@{h}:/var/www/html/'.format(p=path, h=hostname))

    return cmds


def run_remote_commands(commands):
    for cmd in commands:
        outmsg('Command: {c}'.format(c=cmd))
        subprocess.Popen(shlex.split(cmd)).wait()


def outmsg(msg):
    print "[PySync-Helper] ", msg


def main():
    parser = argparse.ArgumentParser()

    # Positional kwargs
    parser.add_argument("code_base",
                        help="The code_base to copy")
    parser.add_argument("hostnames",
                        help="A string of hostnames (comma separated) to sync.")

    args = parser.parse_args()
    commands = get_list_of_commands(args.code_base, args.hostnames)
    run_remote_commands(commands)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        outputmsg("The following error has occurred: {e}".format(e.message))
