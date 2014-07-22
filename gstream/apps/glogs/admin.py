from django.contrib import admin
from gstream.apps.glogs.models import GLog
from gstream.apps.content.admin_helpers import ImageInline


class GLogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'author', 'publish_date')
    raw_id_fields = ('author',)

    fieldsets = (
      ('Title, Author, and Publish Settings', {
          'fields': ('title', 'slug', 'author', 'publish_date','publish')
      }),
      ('Content', {
          'fields': ('content',)
      }),
      ('Location', {
          'fields': ('country','latitude','longitude',)
      }),
   )

    inlines = [
        ImageInline,
    ] 

admin.site.register(GLog, GLogAdmin)
