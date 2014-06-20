from django.contrib import admin
from gstream.apps.carousels.models import Carousel,CarouselImage

class CarouselImageInline(admin.StackedInline):
    model = CarouselImage

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [
        CarouselImageInline,
    ] 

admin.site.register(Carousel, CarouselAdmin)