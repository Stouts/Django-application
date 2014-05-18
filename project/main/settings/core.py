""" Immutable settings. Common for all projects. """

import logging
from os import path as op, walk, listdir


PROJECT_ROOT = op.abspath(op.dirname(op.dirname(op.dirname(__file__))))
PROJECT_NAME = op.basename(PROJECT_ROOT)

ENVIRONMENT_NAME = 'core'

ROOT_URLCONF = "%s.urls" % PROJECT_NAME

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
        'USER': '',
        'PASSWORD': '',
        'TEST_CHARSET': 'utf8',
    }
}


# Caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'KEY_PREFIX': '_'.join((PROJECT_NAME, ENVIRONMENT_NAME))
    }
}

# Media settigns
MEDIA_ROOT = op.join(PROJECT_ROOT, 'media')
STATIC_ROOT = op.join(PROJECT_ROOT, 'static')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Templates settings
TEMPLATE_DIRS = ()
for directory_name in walk(PROJECT_ROOT).next()[1]:
    directory_path = op.join(PROJECT_ROOT, directory_name)
    if 'templates' in listdir(directory_path):
        TEMPLATE_DIRS += (op.join(directory_path, 'templates'),)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)

# Applications
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
)

# Middleware
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Base apps settings
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

# Localization
USE_I18N = True
USE_L10N = True
USE_TZ = True
# MIDDLEWARE_CLASSES += ('django.middleware.locale.LocaleMiddleware',)
TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.i18n',)
LOCALE_PATHS = ()
for directory_name in walk(PROJECT_ROOT).next()[1]:
    directory_path = op.join(PROJECT_ROOT, directory_name)
    if 'locale' in listdir(directory_path):
        LOCALE_PATHS += (op.join(directory_path, 'locale'),)

# Debug
INTERNAL_IPS = ('127.0.0.1',)

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'  # noqa
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'joltem': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'tests': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%d.%m %H:%M:%S',
)
logging.info("Core settings loaded.")
