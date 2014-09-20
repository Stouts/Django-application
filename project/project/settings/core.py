""" Immutable settings. The settings is common for every project. """

import sys
from os import path as op, walk, listdir, makedirs

import logging

# Define some paths
BASE_DIR = op.abspath(op.dirname(op.dirname(op.dirname(__file__))))
PROJECT_NAME = op.basename(BASE_DIR)
PROJECT_ROOT = op.dirname(BASE_DIR)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


ENVIRONMENT_NAME = 'core'
ALLOWED_HOSTS = '.%s.com' % PROJECT_NAME, '.%s.com.' % PROJECT_NAME
ROOT_URLCONF = "%s.urls" % PROJECT_NAME
WSGI_APPLICATION = '%s.wsgi.application' % PROJECT_NAME
SITE_ID = 1

# Setup databases
# ===============
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
        'TEST_CHARSET': 'utf8',
    }
}


# Setup caches
# ============
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'KEY_PREFIX': '_'.join((PROJECT_NAME, ENVIRONMENT_NAME))
    }
}


def Directory(*path):
    """ Create directory if it not exists. """
    path = op.join(*path)
    if not op.exists(path):
        try:
            makedirs(path)
        except OSError:
            logging.warning("%s does not exists.", path)
    return path


# Setup static
# ============
MEDIA_ROOT = Directory(PROJECT_ROOT, 'media')
STATIC_ROOT = Directory(PROJECT_ROOT, 'static')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'


# Setup templates
# ===============
TEMPLATE_DIRS = ()
for directory_name in walk(BASE_DIR).next()[1]:
    directory_path = op.join(BASE_DIR, directory_name)
    if 'templates' in listdir(directory_path):
        TEMPLATE_DIRS += (op.join(directory_path, 'templates'),)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

# Applications
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

# Middlewares
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Base apps settings
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
USE_I18N = True
USE_L10N = True
USE_TZ = True
TIME_ZONE = 'UTC'
# MIDDLEWARE_CLASSES += ('django.middleware.locale.LocaleMiddleware',)
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.i18n', 'django.core.context_processors.tz')
LOCALE_PATHS = ()
for directory_name in walk(BASE_DIR).next()[1]:
    directory_path = op.join(BASE_DIR, directory_name)
    if 'locale' in listdir(directory_path):
        LOCALE_PATHS += (op.join(directory_path, 'locale'),)

# Debug
INTERNAL_IPS = ('127.0.0.1',)

# Logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%d.%m %H:%M:%S',
)
logging.info("Core settings loaded.")
