"""
WSGI config for dj_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.local")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from django.conf import settings

if settings.DEBUG:
    import uwsgi
    from uwsgidecorators import timer
    from werkzeug.debug import DebuggedApplication

    from django.utils import autoreload
    from django.views import debug

    @timer(3)
    def check_code(sig):
        """ Check for code is changed. """
        if autoreload.code_changed():
            uwsgi.reload()

    def null_technical_500_response(request, exc_type, exc_value, tb):
        """ Populate exceptions to werkzeug. """
        raise exc_type, exc_value, tb
    debug.technical_500_response = null_technical_500_response
    application = DebuggedApplication(application, evalex=True)

# pylama:ignore=F0401,E0611
