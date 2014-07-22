
from django.contrib import admin
from gstream.apps.content.models import Image

class ImageInline(admin.TabularInline):
    model = Image
