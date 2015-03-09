# -*- coding: utf-8 -*-
from loading import *  # NOQA

SECRET_KEY = env('SECRET_KEY')


ROOT_URLCONF = 'urls'
TIME_ZONE = 'Europe/Zurich'
LANGUAGE_CODE = 'en'

DEBUG = True
TEMPLATE_DEBUG = True
ADMINS = ()
MANAGERS = ()

USE_I18N = True
USE_L10N = True

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_toolbar',

    'core',
)


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    # debuging middleware
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


TEMPLATE_DIRS = env('TEMPLATE_DIRS', [
    project_path('templates'),
])


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
)


DATABASE_URL = env('DATABASE_URL', 'sqlite:///%s' % project_path('tmp', 'dev.db'))
DATABASES = {'default': dj_database_url.parse(DATABASE_URL)}


# APPS SETTINGS #########################################
# django.contrib.sites
SITE_ID = env('SITE_ID', 1)

# django.contrib.admin
ADMIN_MEDIA_PREFIX = '/static/admin/'

# django debug toolbar
INTERNAL_IPS = (
    '127.0.0.1',
)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS' : False
}

# django.contrib.staticfiles
STATIC_ROOT = project_path('static')
STATIC_URL = '/static/'

# media files
MEDIA_ROOT = project_path('tmp', 'media')
MEDIA_URL = '/media/'
# APPS SETTINGS #########################################
