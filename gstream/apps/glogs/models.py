from django.db import models
from django.core.urlresolvers import reverse
  
from cms.models.pluginmodel import CMSPlugin
from gstream.apps.content.models import ContentObject
from taggit.managers import TaggableManager


class GLog(ContentObject):   
    content = models.TextField()
    tags = TaggableManager()

    def get_absolute_url(self):
       	return reverse('glog-detail', kwargs={'slug' : self.slug})

    def __unicode__(self):
        return self.title


class GLogPlugin(CMSPlugin):
    glog = models.ForeignKey(GLog)
    def __unicode__(self):
        return self.glog.title
