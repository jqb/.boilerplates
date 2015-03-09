# -*- coding: utf-8 -*-
from .common import *  # NOQA


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': projectpath('dev.db'),
    }
}


# devserver staff
INSTALLED_APPS = INSTALLED_APPS + (
    'devserver',
)

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
    'devserver.middleware.DevServerMiddleware',
)
# end devserver staff
