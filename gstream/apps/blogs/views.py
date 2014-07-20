from datetime import datetime

from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.utils.text import slugify
from django.core.urlresolvers import reverse

from models import BlogPost
from forms import BlogForm


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blogs/list.html'
    queryset = BlogPost.objects.filter(publish=True)


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blogs/detail.html'
    queryset = BlogPost.objects.filter(publish=True)
    context_object_name = 'blog_post'


class BlogFormView(FormView):
    form_class = BlogForm
    template_name = 'blogs/edit.html'

    def form_valid(self, form):
    	#import pdb; pdb.set_trace()
    	blog = BlogPost()
    	blog.author = self.request.user
    	blog.title = form.cleaned_data['title']
    	blog.slug = slugify(form.cleaned_data['title'])
    	blog.content = form.cleaned_data['content']
    	blog.publish_date = datetime.now()
    	blog.save()
    	self.blog = blog
    	return super(BlogFormView, self).form_valid(form)

    def get_success_url(self):
    	return reverse('blog-detail', args=(self.blog.slug,))
