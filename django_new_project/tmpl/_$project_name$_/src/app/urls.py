# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include
from django.contrib import admin

from . import views


admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', views.index),
    (r'^admin/', include(admin.site.urls)),
)
