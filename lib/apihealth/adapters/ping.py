import pyping

class PingAdapter(object):
    @staticmethod
    def ping_url(url):
        try:
            # TODO: Add something for packet loss
            result = pyping.ping(url, udp=True)
            if result.ret_code != 0:
                # Can't be reached
                health = 1
            else:
                health = 0
        except:
            # URL not found
            health = 1
        finally:
            return health
