from datetime import datetime

from django.views.generic import (
        CreateView,
        UpdateView, 
        ListView, 
        DetailView, 
        FormView
    )
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from models import GLog
from forms import GLogForm


class GLogListView(ListView):
    model = GLog
    queryset = GLog.objects.filter(publish=True)


class GLogCreateView(CreateView):
    model = GLog
    form_class = GLogForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.cleaned_data['title'])
        form.instance.publish_date = datetime.now()
        form.instance.publish = True
        return super(GLogCreateView, self).form_valid(form)  


class GLogUpdateView(UpdateView):
    model = GLog
    form_class = GLogForm

    def get_object(self, queryset=None):
        obj = GLog.objects.get(id=self.kwargs['id'])
        return obj

    def form_valid(self, form):
        form.instance.slug = slugify(form.cleaned_data['title'])
        
        return super(GLogUpdateView, self).form_valid(form)   


class GLogDetailView(DetailView):
    model = GLog
    queryset = GLog.objects.filter(publish=True)


class GLogFormView(FormView):
    form_class = GLogForm
    template_name = 'glogs/edit.html'

    def dispatch(self, request, *args, **kwargs):
        if 'id' in kwargs.keys():
            self.id = kwargs.pop('id')
        else:
            self.id = None
        return super(GLogFormView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
    	#import pdb; pdb.set_trace()
    	glog = GLog()
    	glog.author = self.request.user
    	glog.title = form.cleaned_data['title']
    	glog.slug = slugify(form.cleaned_data['title'])
    	glog.content = clean_html(form.cleaned_data['content'])
    	glog.publish_date = datetime.now()
    	glog.save()
    	self.glog = glog
    	return super(GLogFormView, self).form_valid(form)

    def get_success_url(self):
    	return reverse('glog-detail', args=(self.glog.slug,))
