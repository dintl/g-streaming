from django.conf.urls import patterns, include, url

from views import MyGStreamingView

urlpatterns = patterns('',
    url(r'^$', MyGStreamingView.as_view(), name='mygstreaming'),
)
