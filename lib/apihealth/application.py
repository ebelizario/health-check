'''Application layer'''

import os
import sys

sys.path.insert(0, os.path.realpath(
                os.path.dirname(__file__)) + '/../../conf')


def check_health(context, url, title):
    return context.api_check_handler.getHealth(url)
