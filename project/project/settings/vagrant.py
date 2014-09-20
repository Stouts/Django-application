""" Vagrant settings. """

from .develop import *


ENVIRONMENT_NAME = 'vagrant'

CACHES['KEY_PREFIX'] = '_'.join((PROJECT_NAME, ENVIRONMENT_NAME))

logging.info("Production settings are loaded.")

# pylama:ignore=W0401,W0614
