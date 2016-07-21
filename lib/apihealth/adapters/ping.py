import pyping

class PingAdapter(object):
    @staticmethod
    def ping_url(url):
        try:
            # TODO: Add something for packet loss
            result = pyping.ping(url, udp=True)
            if result.ret_code == 0:
                health = 0
                avg_rtt = result.avg_rtt
            else:
                health = 1
                avg_rtt = 'N/A'
        except:
            # URL not found
            health = 1
            avg_rtt = 'N/A'
        finally:
            return health, avg_rtt
