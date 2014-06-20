from django.db import models
from easy_thumbnails.fields import ThumbnailerField
from cms.models.pluginmodel import CMSPlugin

class Carousel(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class CarouselImage(models.Model):

    TARGET_CHOICES = (
        ('_blank', 'New Window'),
        ('_self', 'Same Window'),
    )

    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    target = models.CharField(max_length=10, choices=TARGET_CHOICES)
    image = ThumbnailerField(upload_to='carousel_images')
    carousel = models.ForeignKey(Carousel, related_name="images")

    def __unicode__(self):
        return self.title

class CarouselPlugin(CMSPlugin):
    carousel = models.ForeignKey(Carousel)
    def __unicode__(self):
        return self.carousel.name