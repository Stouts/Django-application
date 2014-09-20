# This is necessary to satisfy py.test, when running tests.
# http://pytest-django.readthedocs.org/en/latest/faq.html#i-see-an-error-saying-could-not-import-myproject-settings
# There have been many requests to extend/modify py.test to avoid having to do this. There is a lot of
# resistance, because adding 'cwd' to the path is generally unexpected for scripts that may be run anywhere.

from distutils.core import setup
setup(name='project_for_pytest', version='1.0')

