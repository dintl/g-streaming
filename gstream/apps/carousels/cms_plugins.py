from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import CarouselPlugin

class CarouselPlugin(CMSPluginBase):
    model = CarouselPlugin
    name = "Carousel"
    render_template = "carousels/carousel.html"

    def render(self, context, instance, placeholder):
        context['carousel'] = instance.carousel
        return context

plugin_pool.register_plugin(CarouselPlugin)
