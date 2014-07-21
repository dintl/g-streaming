from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import GLogPlugin

class GLogPlugin(CMSPluginBase):
    model = GLogPlugin
    name = "GLog"
    render_template = "glogs/preview.html"

    def render(self, context, instance, placeholder):
        context['glog'] = instance.glog
        return context

plugin_pool.register_plugin(GLogPlugin)