from django.conf.urls import patterns, include, url

from views import BlogListView, BlogDetailView, BlogFormView

urlpatterns = patterns('',
    url(r'^$', BlogListView.as_view(), name='blog-list'),
    url(r'^create/$', BlogFormView.as_view(), name='blog-create'),
    url(r'^edit/(?P<id>\d+)/$', BlogFormView.as_view(), name='blog-edit'),
    url(r'^(?P<slug>[\w-]+)/$', BlogDetailView.as_view(), name='blog-detail'),
)