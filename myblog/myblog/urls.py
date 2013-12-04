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
