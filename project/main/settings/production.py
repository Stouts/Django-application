""" Production settings. """

from .core import *


ENVIRONMENT_NAME = 'production'

SECRET_KEY = 'DontForgetToReplaceMe'

CACHES['KEY_PREFIX'] = '_'.join((PROJECT_NAME, ENVIRONMENT_NAME))

ROOT_URLCONF = "main.urls"

# Bootstrap
INSTALLED_APPS += 'bootstrap3',

# File browser
INSTALLED_APPS = ('filebrowser',) + INSTALLED_APPS
FILEBROWSER_DIRECTORY = op.join(MEDIA_ROOT, 'uploads')

# Grappelli
INSTALLED_APPS = ('grappelli.dashboard', 'grappelli') + INSTALLED_APPS
GRAPPELLI_INDEX_DASHBOARD = 'main.dashboard.CustomIndexDashboard'
GRAPPELLI_ADMIN_TITLE = PROJECT_NAME
GRAPPELLI_SWITCH_USER = True


logging.info("Production settings are loaded.")

# pylama:ignore=W0401,W0614
