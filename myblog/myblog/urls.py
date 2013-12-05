# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # admin app
    url(r'^admin/', include(admin.site.urls)),

    # blog app
    url(r'^', include('apps.blog.urls')),
)

#from django.conf import settings
#urlpatterns += patterns(
#    '',
#    (
#        r'^media/(?P<path>.*)$',
#        'django.views.static.serve',
#        {
#            'document_root': settings.MEDIA_ROOT,
#            'show_indexes': True
#        }
#    ),
#)
