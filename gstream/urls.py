from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'gstream.apps.home.views.homepage', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('gstream.apps.accounts.urls')),

    url(r'^', include('cms.urls')),
)


if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns