class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

HEALTH_LABEL = {
    0: ('OK', bcolors.OKGREEN, bcolors.ENDC),
    1: ('BAD', bcolors.FAIL, bcolors.ENDC),
    2: ('Intermittent', bcolors.WARNING, bcolors.ENDC)
}

API_URLS = [
    ('Conflict', 'cmaas-conflict-api.cm.comcast.net'),
    ('TTS API', 'cmaas-tts-api.cm.comcast.net'),
    ('Dependency', 'cmaas-dependency-api.cm.comcast.net'),
    ('Watchlist', 'cmaas-watchlist-api.cm.comcast.net'),
    ('Element', 'cmaas-element-api.cm.comcast.net'),
    ('Reservation', 'cmaas-reservation-api.cm.comcast.net'),
    ('Customer', 'customer-api.cm.comcast.net'),
    ('Market Lookup', 'marketlookup-api.cm.comcast.net'),
]
