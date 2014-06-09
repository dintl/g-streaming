from django.contrib import admin
from django.utils.safestring import mark_safe
from django.core import urlresolvers

from . import models

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location_country')
    search_fields  = ['user__username', 'location_country__common_name']
    list_filter = ['location_country__common_name',]
    readonly_fields = ['user','user_link']

    def user_link(self, obj):
        change_url = urlresolvers.reverse('admin:auth_user_change', args=(obj.user.id,))
        return mark_safe('<a href="%s">%s</a>' % (change_url, change_url))
    user_link.short_description = 'Django User Link'
    user_link.allow_tags = True
   
admin.site.register(models.UserProfile, UserProfileAdmin)
