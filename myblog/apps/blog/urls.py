# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns(
    'apps.blog.views',

    url(r'^$', 'post_list', name='blog_post_list'),

    url(
        r'^(?P<slug>[-\w]+)/$', 'post_detail',
        name='blog_post_detail'
    ),
)
