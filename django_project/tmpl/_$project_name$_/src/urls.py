# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', TemplateView.as_view(template_name='base.html')),
)
