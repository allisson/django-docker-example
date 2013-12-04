# -*- coding: utf-8 -*-
from django.contrib import admin

from apps.blog.models import Post


class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'published')
    list_filter = ('published',)


admin.site.register(Post, PostAdmin)
