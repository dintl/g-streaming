from django.views.generic import TemplateView
from gstream.apps.blogs.models import BlogPost

class MyGStreamingView(TemplateView):

    template_name = "mygstreaming/overview.html"

    def get_context_data(self, **kwargs):
        context = super(MyGStreamingView, self).get_context_data(**kwargs)
        context['blogs'] = BlogPost.objects.filter(author=self.request.user)
        return context
