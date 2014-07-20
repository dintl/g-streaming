from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import mail_managers, send_mail
from django.db import models
from easy_thumbnails.fields import ThumbnailerField

from gstream.apps.locations.mixins import LocationMixin


class Interest(models.Model):
    interest = models.CharField(max_length=140)

    def __unicode__(self):
        return self.interest

class Profile(LocationMixin):


    LOCATION_PRIVACY_CHOICES = (('none', "Private - Don't share my location at all"),
                                ('anonymous', "Anonymous - Share my location anonymously"),
                                ('public', "Public - Share my location with my profile information"),)

    user        = models.OneToOneField(User)
    photo       = ThumbnailerField(upload_to='profile_photos',blank=True)
    bio         = models.TextField(blank=True, null=True)
    city        = models.CharField(max_length=200, blank=True)
    interests   = models.ManyToManyField(Interest, blank=True)
    location_privacy  = models.CharField(max_length=20, default='anonymous', choices=LOCATION_PRIVACY_CHOICES)

    def __unicode__(self):
        return u"User profile for %s" % self.user
