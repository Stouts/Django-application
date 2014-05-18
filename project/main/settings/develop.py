""" Develop settings. """

from .production import *


ENVIRONMENT_NAME = 'develop'

DEBUG = True
TEMPLATE_DEBUG = DEBUG
TEMPLATE_CONTEXT_PROCESSORS += 'django.core.context_processors.debug',
MIDDLEWARE_CLASSES += 'debug_toolbar.middleware.DebugToolbarMiddleware',
INSTALLED_APPS += 'debug_toolbar', 'django_extensions'
DEBUG_TOOLBAR_PATCH_SETTINGS = False
INTERNAL_IPS = '127.0.0.1', '33.33.33.1'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Logging
LOGGING['loggers']['django.request']['level'] = 'WARNING'
LOGGING['loggers']['django.db.backends'] = {
    'handlers': ['console'],
    'level': 'WARNING'
}

# Caches
CACHES['default']['KEY_PREFIX'] = '_'.join((PROJECT_NAME, ENVIRONMENT_NAME))

# Let cookie to be sent via http
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

logging.info('Develop settings are loaded.')

# pylama:ignore=W0401,W0614
