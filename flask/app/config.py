class Common(object):
    DEBUG = False

class Development(Common):
    DEBUG = True

class Production(Common):
    DEBUG = False