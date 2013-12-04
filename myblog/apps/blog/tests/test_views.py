# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse

from model_mommy import mommy

from apps.blog.models import Post


class PostListTest(TestCase):

    def setUp(self):
        self.posts = mommy.make(
            Post,
            published=True,
            slug='',
            _quantity=5,
        )
        self.url = reverse('blog_post_list')

    def test_render(self):
        response = self.client.get(self.url)
        self.assertTrue(response.context['post_list'])
        self.assertEqual(len(response.context['post_list']), 5)


class PostDetailTest(TestCase):

    def setUp(self):
        self.post = mommy.make(
            Post,
            published=True,
            slug=''
        )
        self.url = reverse('blog_post_detail', args=[self.post.slug])

    def test_render(self):
        response = self.client.get(self.url)
        self.assertTrue(response.context['post'])
        self.assertEqual(response.context['post'], self.post)
