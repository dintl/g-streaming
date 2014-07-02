from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import BlogPostPlugin

class BlogPostPlugin(CMSPluginBase):
    model = BlogPostPlugin
    name = "BlogPost"
    render_template = "blogs/preview.html"

    def render(self, context, instance, placeholder):
        context['blog_post'] = instance.blog_post
        return context

plugin_pool.register_plugin(BlogPostPlugin)