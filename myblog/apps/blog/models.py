# -*- coding: utf-8 -*-
from django.db import models

from autoslug import AutoSlugField


class Post(models.Model):

    title = models.CharField(
        u'Título',
        max_length=200
    )

    slug = AutoSlugField(
        populate_from='title',
        unique=True
    )

    content = models.TextField(
        u'Conteúdo'
    )

    published = models.BooleanField(
        u'Publicado',
        default=True
    )

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Post'
        verbose_name_plural = u'Posts'
