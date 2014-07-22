from django.conf.urls import patterns, include, url

from views import GLogListView, GLogDetailView, GLogCreateView, GLogUpdateView

urlpatterns = patterns('',
    url(r'^$', GLogListView.as_view(), name='glog-list'),
    url(r'^create/$', GLogCreateView.as_view(), name='glog-create'),
    url(r'^edit/(?P<id>\d+)/$', GLogUpdateView.as_view(), name='glog-edit'),
    url(r'^(?P<slug>[\w-]+)/$', GLogDetailView.as_view(), name='glog-detail'),
)