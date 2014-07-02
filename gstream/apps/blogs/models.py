from django.db import models
from cms.models.pluginmodel import CMSPlugin
from gstream.apps.content.models import ContentItem

class BlogPost(ContentItem):   
    content = models.TextField()
    def __unicode__(self):
        return self.title

class BlogPostPlugin(CMSPlugin):
    blog_post = models.ForeignKey(BlogPost)
    def __unicode__(self):
        return self.blog_post.title
