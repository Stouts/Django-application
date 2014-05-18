""" Integrate celery. """

from __future__ import absolute_import, print_function

import os

from celery import Celery

from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.main.settings.local')

app = Celery(settings.PROJECT_NAME)

app.config_from_object(settings)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    """ Debug celery. """
    print('Request: {0!r}'.format(self.request))
