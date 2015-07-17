""" Syncfiles

This defines the class that will sync files from a code base to a server

"""

import os
import re
import shlex
import config
import subprocess
import argparse


class Syncfiles(object):

    def __init__(self, code_base, device_ip, remote_boxes="",
                 print_only=False):
        self.code_base = code_base
        self.device_ip = device_ip
        self.remote_boxes = remote_boxes
        self.print_only = print_only

    def sync_files_to_server(self):
        """Syncs files to server
        """
        cmds = []
        box_list = []
        local_code_base_path = config.LOCAL_PATH[self.code_base]
        remote_code_base_path = config.REMOTE_PATH[self.code_base]
        pysynchelper_path = os.path.join(config.LOCAL_PYSYNCHELPER_PATH,
                                         'pysynchelper.py')

        # Create list of remote boxes and reverse list to put SSRs in front
        if self.remote_boxes:
            box_list = sorted(self.remote_boxes.split(','), reverse=True)

        # Validate list of remote boxes
        if not self.validate_boxes(box_list):
            raise Exception("An invalid remote box was found.")

        # Add command for device_ip first
        cmds.append('rsync -{o} --del {e} {l} root@{d}:{r}'
                    .format(o=config.RSYNC_OPTIONS,
                            e=Syncfiles.build_excludes_from_list(),
                            l=local_code_base_path,
                            d=self.device_ip,
                            r=remote_code_base_path))

        # Add commands for remote boxes
        if self.remote_boxes:
            # Add command to copy helper script to device_ip in /tmp
            cmds.append('scp {p} root@{d}:/tmp/'.format(p=pysynchelper_path,
                                                        d=self.device_ip))

            # Create hostname list for each box in box_list
            hostnames = Syncfiles.create_hostnames_list(box_list)

            # Add command to execute helper script with list of hostnames
            cmds.append('ssh root@{d} "{r} /tmp/pysynchelper.py {c} {h}"'
                        .format(d=self.device_ip,
                                r=config.REMOTE_PYTHON_PATH,
                                c=self.code_base,
                                h=",".join(hostnames)))

        Syncfiles.outmsg("Commands to run")

        # Execute or test all commands
        for cmd in cmds:
            Syncfiles.outmsg("Command: {c}".format(c=cmd))
            if not self.print_only:
                subprocess.Popen(shlex.split(cmd)).wait()

    @staticmethod
    def build_excludes_from_list():
        """Builds string of rsync excludes from config
        """
        return ' '.join(["--exclude='" + s + "'" for s in config.SYNC_EXCLUDES])

    @staticmethod
    def create_hostnames_list(box_list):
        hostnames = []
        for box in box_list:
            if re.match('^[a-z]{1}$', box):
                box_hostname = 'ssr{b}'.format(b=box)
            else:
                box_hostname = 'ssb{b}'.format(b=box)
            hostnames.append(box_hostname)
        return hostnames

    @staticmethod
    def get_args():
        """ Returns incoming arguments as Namespace object
        """
        parser = argparse.ArgumentParser()

        # Positional kwargs
        parser.add_argument("code_base", choices=["tools", "admin"],
                            help="The code base to sync")
        parser.add_argument("device_ip",
                            help="The IP address of the first device to sync.")

        # Optional args
        parser.add_argument("-r", "--remote_boxes", type=str,
                            help="Comma separated list of remote boxes to "
                            "sync to. Example: b,1,2")
        parser.add_argument("--print_only", action="store_true",
                            default=False,
                            help="Output but do not execute commands.")

        return parser.parse_args()

    def validate_boxes(self, box_list):
        """Validates a list of box letters/numbers
        """
        allowed_boxes = {
            'admin': '^[a-f]{1}$',
            'tools': '^([a-f]{1}|[1-9]|[1-2][0-9]|30)$'
        }

        for box in box_list:
            if not re.match(allowed_boxes[self.code_base], box):
                return False

        return True

    @staticmethod
    def outmsg(msg):
        print "[PySync] ", msg
