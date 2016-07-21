#!/usr/bin/python2.7
'''
Get health of our APIs
'''

import multiprocessing
import os
import sys

sys.path.insert(0, os.path.realpath(
                os.path.dirname(__file__)) + '/../lib')
sys.path.insert(0, os.path.realpath(
                os.path.dirname(__file__)) + '/../conf')

from apihealth.adapters.ping import PingAdapter
from apihealth.application import check_health
from apihealth.handlers import Context, ApiHealthCheck
from config import API_URLS, HEALTH_LABEL

context = Context()
context.api_check_handler = ApiHealthCheck(PingAdapter())


def check_all_apis():
    '''Enumerate all urls in config'''
    threads = []
    for title, url in API_URLS:
        job = multiprocessing.Process(
            target=_check_health_job,
            args=(context, url, title),
        )
        threads.append(job)
        job.start()


def _check_health_job(context, url, title):
    '''Single job for multi-threaded use'''
    result, avg_time = check_health(context, url, title)
    print_results(title, result, avg_time)


def print_header():
    print "\t\t".join(["API", "Status", "Avg Time"])
    print "\t\t".join(["---", "------", "--------"])


def print_results(title, result, avg_time):
    print "{title} \t{result} \t\t{avg_time}".format(
        title=title,
        result=_map_health_label(result),
        avg_time=avg_time,
    )


def _map_health_label(result):
    return HEALTH_LABEL[result][1] + HEALTH_LABEL[result][0] + HEALTH_LABEL[result][2]


def main():
    # TODO: Add options for single url testing
    print_header()
    check_all_apis()


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print "Something went wrong: {err}".format(err=err)
