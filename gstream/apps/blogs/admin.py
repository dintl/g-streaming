from django.contrib import admin
from gstream.apps.blogs.models import BlogPost
from gstream.apps.content.admin_helpers import ImageInline, TagInline


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date')
    inlines = [
        ImageInline,
        TagInline
    ] 

admin.site.register(BlogPost, BlogPostAdmin)
