""" Production settings. """

from .core import *


ENVIRONMENT_NAME = 'production'

SECRET_KEY = 'DontForgetToReplaceMe'

CACHES['default']['KEY_PREFIX'] = '_'.join((PROJECT_NAME, ENVIRONMENT_NAME))

ROOT_URLCONF = "%s.main.urls" % PROJECT_NAME

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

SITE_ID = 1

INSTALLED_APPS += (
    # Project
    '%s.main' % PROJECT_NAME,
)

# Bootstrap
INSTALLED_APPS += 'bootstrap3',

# File browser
INSTALLED_APPS = ('filebrowser',) + INSTALLED_APPS
FILEBROWSER_DIRECTORY = Directory(MEDIA_ROOT, 'uploads')

# Grappelli
INSTALLED_APPS = ('grappelli.dashboard', 'grappelli') + INSTALLED_APPS
GRAPPELLI_INDEX_DASHBOARD = '%s.main.dashboard.CustomIndexDashboard' % PROJECT_NAME # noqa
GRAPPELLI_ADMIN_TITLE = PROJECT_NAME
GRAPPELLI_SWITCH_USER = True

# Dealer
TEMPLATE_CONTEXT_PROCESSORS += 'dealer.contrib.django.context_processor',

# Django allauth
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = "[%s]" % PROJECT_NAME
TEMPLATE_DIRS = (op.join(APPS_ROOT, 'main', 'templates', 'allauth'),) + TEMPLATE_DIRS  # noqa
TEMPLATE_CONTEXT_PROCESSORS += (
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
)
AUTHENTICATION_BACKENDS += (
    'allauth.account.auth_backends.AuthenticationBackend',
)
INSTALLED_APPS += (
    'django.contrib.sites',
    'bootstrapform',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.bitbucket',
    'allauth.socialaccount.providers.github',
)


logging.info("Production settings are loaded.")

# pylama:ignore=W0401,W0614
