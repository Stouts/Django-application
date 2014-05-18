""" Project urls. """

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from filebrowser.sites import site


urlpatterns = [
    url(r'^$', 'main.views.index', name='home'),
    url(r'^desk/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^desk/', include(admin.site.urls)),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),

        url(r'^__debug__/', include(debug_toolbar.urls))
    ]
