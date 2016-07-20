class ApiHealthCheck(object):
    """ Base SQL Alchemey class """
    def __init__(self, adapter):
        self.adapter = adapter

    def getHealth(self, url):
        return self.adapter.ping_url(url)
