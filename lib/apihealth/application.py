'''Application layer'''

import os
import sys

sys.path.insert(0, os.path.realpath(
                os.path.dirname(__file__)) + '/../../conf')

from config import HEALTH_LABEL


def print_header():
    print "\t\t".join(["API", "Status"])
    print "\t\t".join(["---", "------"])


def check_health(context, url, title):
    result = context.api_check_handler.getHealth(url)
    _print_results(result, url, title)


def _print_results(result, url, title):
    print "{title} \t{result}".format(
        title=title,
        url=url,
        result=_map_health_label(result)
    )


def _map_health_label(result):
    return HEALTH_LABEL[result][1] + HEALTH_LABEL[result][0] + HEALTH_LABEL[result][2]
