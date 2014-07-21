from django.db import models
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerField
from gstream.apps.locations.mixins import LocationMixin

class ContentObject(LocationMixin):
    slug = models.SlugField()
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User)
    publish_date = models.DateField()
    publish = models.BooleanField(default=True)
    content_type = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.content_type = 'glog'
    	super(ContentObject, self).save(*args, **kwargs)
    	

class Image(models.Model):
    image = ThumbnailerField(upload_to='images')
    caption = models.CharField(max_length=500, blank=True, null=True)
    content_object = models.ForeignKey(ContentObject, related_name='images')
   
    def __unicode__(self):
        return self.caption

class Tag(models.Model):
    tag = models.CharField(max_length=100)
    content_object = models.ForeignKey(ContentObject)

    def __unicode__(self):
        return self.tag

class Favorite(models.Model):
	user = models.ForeignKey(User)
	content_object = models.ForeignKey(ContentObject)
