from apihealth.handlers.api_health import ApiHealthCheck

class Context(object):
    """ Placeholder for context """
    def __init__(self):
        self._api_check_handler = None

    @property
    def api_check_handler(self):
        if not self._api_check_handler:
            raise NotImplementedError("No API Check Handler exists")
        return self._api_check_handler

    @api_check_handler.setter
    def api_check_handler(self, api_check_handler):
        self._api_check_handler = api_check_handler
