# -*- coding: utf-8 -*-
from django.views.generic import TemplateView


index = TemplateView.as_view(template_name='base.html')
