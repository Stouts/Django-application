from django.core.management import BaseCommand


class Command(BaseCommand):

    """ Create development data. """

    def handle(self, **kwargs):
        from main.utils.mixer import mixer

        with mixer.ctx(loglevel='INFO'):

            # Admin user
            mixer.guard(username='admin').blend(
                'auth.user', username='admin', email='admin@google.com', password='pass',
                is_staff=True, is_superuser=True)

            # Simple user
            mixer.guard(username='user').blend(
                'auth.user', username='user', email='user@google.com', password='pass')
