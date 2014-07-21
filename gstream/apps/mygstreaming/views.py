from django.views.generic import TemplateView
from gstream.apps.glogs.models import GLog

class MyGStreamingView(TemplateView):

    template_name = "mygstreaming/overview.html"

    def get_context_data(self, **kwargs):
        context = super(MyGStreamingView, self).get_context_data(**kwargs)
        context['glogs'] = GLog.objects.filter(author=self.request.user)
        return context
