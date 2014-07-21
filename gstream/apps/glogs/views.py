from datetime import datetime

from django.views.generic import CreateView, ListView, DetailView, FormView
from django.utils.text import slugify
from django.core.urlresolvers import reverse

from models import GLog
from forms import BlogForm


class BlogListView(ListView):
    #This uses the template glogs/glog_list.html by default
    model = GLog
    queryset = GLog.objects.filter(publish=True)


class BlogDetailView(DetailView):
    model = GLog
    template_name = 'glogs/detail.html'
    queryset = GLog.objects.filter(publish=True)
    context_object_name = 'glog'


class BlogFormView(FormView):
    form_class = BlogForm
    template_name = 'glogs/edit.html'

    def dispatch(self, request, *args, **kwargs):
        
        if 'id' in kwargs.keys():
            self.id = kwargs.pop('id')
        else:
            self.id = None

        return super(BlogFormView, self).dispatch(request, *args, **kwargs)

   

    def form_valid(self, form):
    	#import pdb; pdb.set_trace()
    	glog = GLog()
    	glog.author = self.request.user
    	glog.title = form.cleaned_data['title']
    	glog.slug = slugify(form.cleaned_data['title'])
    	glog.content = form.cleaned_data['content']
    	glog.publish_date = datetime.now()
    	glog.save()
    	self.glog = glog
    	return super(BlogFormView, self).form_valid(form)

    def get_success_url(self):
    	return reverse('glog-detail', args=(self.glog.slug,))
