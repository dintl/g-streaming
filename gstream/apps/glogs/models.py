from django.db import models
from cms.models.pluginmodel import CMSPlugin
from gstream.apps.content.models import ContentObject

class GLog(ContentObject):   
    content = models.TextField()
    def __unicode__(self):
        return self.title

class GLogPlugin(CMSPlugin):
    glog = models.ForeignKey(GLog)
    def __unicode__(self):
        return self.glog.title
