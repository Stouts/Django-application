""" Settings for tests running. """

from .production import *


ENVIRONMENT_NAME = "test"

# Databases
DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
DATABASES['default']['NAME'] = ':memory:'

# Caches
CACHES['default']['BACKEND'] = 'django.core.cache.backends.locmem.LocMemCache'
CACHES['default']['KEY_PREFIX'] = '_'.join((PROJECT_NAME, ENVIRONMENT_NAME))

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# Disable south migrations on db creation in tests
SOUTH_TESTS_MIGRATE = False

# Celery
CELERY_ALWAYS_EAGER = True

logging.info("Test settings are loaded.")

# pylama:ignore=W0401,W0614
