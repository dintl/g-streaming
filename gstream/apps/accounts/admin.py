from django.contrib import admin
from django.utils.safestring import mark_safe
from django.core import urlresolvers

from . import models

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'country')
    search_fields  = ('user__username', 'country__common_name')
    readonly_fields = ('user_link',)
    list_filter = ('interests',)

    def user_link(self, obj):
        change_url = urlresolvers.reverse('admin:auth_user_change', args=(obj.user.id,))
        return mark_safe('<a href="%s">%s</a>' % (change_url, change_url))
    user_link.short_description = 'Django User Link'
    user_link.allow_tags = True
   

class InterestAdmin(admin.ModelAdmin):
	list_display=('interest',)

admin.site.register(models.Profile, ProfileAdmin)
admin.site.register(models.Interest, InterestAdmin)