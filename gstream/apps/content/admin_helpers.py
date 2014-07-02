
from django.contrib import admin
from gstream.apps.content.models import Image, Tag

class ImageInline(admin.TabularInline):
    model = Image

class TagInline(admin.TabularInline):
    model = Tag