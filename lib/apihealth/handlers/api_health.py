class ApiHealthCheck(object):
    '''API Health Check Handler'''
    def __init__(self, adapter):
        self.adapter = adapter

    def getHealth(self, url):
        return self.adapter.ping_url(url)
