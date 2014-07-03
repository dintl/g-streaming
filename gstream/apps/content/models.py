from django.db import models
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerField
from gstream.apps.locations.mixins import LocationMixin

class ContentItem(LocationMixin):
    slug = models.SlugField()
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User)
    publish_date = models.DateField()
    publish = models.BooleanField(default=True)
    content_type = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.content_type = 'blog'
    	super(ContentItem, self).save(*args, **kwargs)
    	

class Image(models.Model):
    image = ThumbnailerField(upload_to='images')
    caption = models.CharField(max_length=500, blank=True, null=True)
    content_item = models.ForeignKey(ContentItem, related_name='images')
   
    def __unicode__(self):
        return self.caption

class Tag(models.Model):
    tag = models.CharField(max_length=100)
    content_item = models.ForeignKey(ContentItem)

    def __unicode__(self):
        return self.tag

class Favorite(models.Model):
	user = models.ForeignKey(User)
	content_item = models.ForeignKey(ContentItem)
