""" Init wsgi application. """
import os.path
import sys

from main.wsgi import application


sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'project'))


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
