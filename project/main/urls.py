""" Project urls. """
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from filebrowser.sites import site


urlpatterns = [
    url(r'^$', 'project.main.views.index', name='home'),
    url(r'^desk/filebrowser/', include(site.urls)),
    url(r'^accounts/profile/', 'project.main.views.index', name='profile'),
]

# Allauth
urlpatterns.append(
    url(r'^accounts/', include('allauth.urls'))
)

# Django admin
admin.autodiscover()
urlpatterns += [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^desk/', include(admin.site.urls)),
]


# Debug tools
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'), 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

        url(r'^%s/(?P<path>.*)$' % settings.STATIC_URL.strip('/'),
            'django.contrib.staticfiles.views.serve'),

        url(r'^__debug__/', include(debug_toolbar.urls))
    ]
