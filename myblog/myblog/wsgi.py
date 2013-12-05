# -*- coding: utf-8 -*-
"""
WSGI config for myblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")

from django.core.wsgi import get_wsgi_application
from django.conf import settings

from static import Cling


STATIC_ROOT = settings.STATIC_ROOT
STATIC_URL = settings.STATIC_URL
MEDIA_ROOT = settings.MEDIA_ROOT
MEDIA_URL = settings.MEDIA_URL

static_cling = Cling(STATIC_ROOT + '/')
media_cling = Cling(MEDIA_ROOT + '/')


class ServeStaticMiddleware(object):

    def __init__(self, application):
        self.application = application

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO', '')
        if path.startswith(STATIC_URL) and not settings.DEBUG:
            environ['PATH_INFO'] = path.replace(STATIC_URL, '')
            return static_cling(environ, start_response)
        elif path.startswith(MEDIA_URL) and not settings.DEBUG:
            environ['PATH_INFO'] = path.replace(MEDIA_URL, '')
            return media_cling(environ, start_response)

        return self.application(environ, start_response)


application = ServeStaticMiddleware(get_wsgi_application())
#application = get_wsgi_application()
