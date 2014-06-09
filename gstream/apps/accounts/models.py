
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import mail_managers, send_mail
from django.db import models

from gstream.apps.locations.models import Country

#Monkey patch the User class for django 1.6
def get_profile(self):
    if not hasattr(self, 'profile'):
        self.profile = self.profile_set.all()[0]
    return self.profile
User.get_profile = get_profile
class UserProfile(models.Model):


    LOCATION_PRIVACY_CHOICES = (('none', "Private - Don't share my location at all"),
                                ('anonymous', "Anonymous - Share my location anonymously"),
                                ('public', "Public - Share my location with my profile information"),)

    user        = models.ForeignKey(User)
    city        = models.CharField(max_length=200, blank=True)
    country     = models.CharField(max_length=80)
     
    location_latitude     = models.DecimalField(
        null=True, blank=True, max_digits=8, decimal_places=5
    )
    location_longitude     = models.DecimalField(
        null=True, blank=True, max_digits=8, decimal_places=5
    )
    location_country     = models.ForeignKey(Country, blank=True, null=True)

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
http://g-streaming.net/admin/accounts/userprofile/%s/

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
            
   
    
    
