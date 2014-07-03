from django.conf.urls import patterns, include, url

from views import BlogList, BlogDetail

urlpatterns = patterns('',
    url(r'^$', BlogList.as_view(), name='blog-list'),
    url(r'^(?P<slug>[\w-]+)/$', BlogDetail.as_view(), name='blog-detail'),
)