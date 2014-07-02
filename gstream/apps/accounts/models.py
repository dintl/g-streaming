from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import mail_managers, send_mail
from django.db import models
from easy_thumbnails.fields import ThumbnailerField

from gstream.apps.locations.mixins import LocationMixin


#Monkey patch the User class for django 1.6
def get_profile(self):
    try:
        return self.profile
    except:
        return None
User.get_profile = get_profile

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
    city        = models.CharField(max_length=200, blank=True)
    interests   = models.ManyToManyField(Interest, blank=True)
    location_privacy  = models.CharField(max_length=20, default='anonymous', choices=LOCATION_PRIVACY_CHOICES)

    def __unicode__(self):
        return u"User profile for %s" % self.user


# Notify a user their status has changed to active
@receiver(pre_save, sender=User)
def user_pre_save(sender, instance, signal, *args, **kwargs):

    try:
        #instance is the record about to be saved
        #compare user is the record in the db
        compare_user = User.objects.get(pk=instance.id)
    except:
        #returns if user is new or fixture is being loaded
        return
    
    if compare_user.is_active != instance.is_active and instance.is_active == True:
        #Mail the admin
        mail_managers('G-Streaming New User "%s" APPROVED' % instance.username,
                      """
Dear G-Streaming Admin,

A new user has been correctly approved for your website.

You can view the user's information here:
Django User
http://g-streaming.net/admin/auth/user/%s/
User Profile
http://g-streaming.net/admin/accounts/profile/%s/

""" % (instance.id, instance.get_profile().id),
                     fail_silently=False)
        
        #Mail the new user
        send_mail('G-Streaming  account "%s" approved!' % instance.username,
                      """
Dear %s,

Your account has been approved at www.g-streaming.net

You may login at the following link:

http://www.g-streaming.net/accounts/login/

""" % instance.username, 
                    'no-reply@g-streaming.net',
                     [instance.email], 
                     fail_silently=False)
            
   
    
    
