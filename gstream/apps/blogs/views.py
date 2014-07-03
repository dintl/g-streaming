from django.views.generic import ListView,  DetailView
from django.views.generic.detail import SingleObjectMixin
from models import BlogPost


class BlogList(ListView):
    model = BlogPost
    template_name = 'blogs/list.html'
    queryset = BlogPost.objects.filter(publish=True)


class BlogDetail(DetailView):
    model = BlogPost
    template_name = 'blogs/detail.html'
    queryset = BlogPost.objects.filter(publish=True)
    context_object_name = 'blog_post'