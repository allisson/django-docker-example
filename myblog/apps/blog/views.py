# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from django.http import Http404

from apps.blog.models import Post


class PostListView(ListView):

    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(published=True)


class PostDetailView(DetailView):

    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')

        try:
            post = Post.objects.get(slug=slug, published=True)
        except Post.DoesNotExist:
            raise Http404

        return post


post_list = PostListView.as_view()
post_detail = PostDetailView.as_view()
