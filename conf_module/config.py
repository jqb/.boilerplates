# -*- coding: utf-8 -*-
import boilerplate

class Configuration(boilerplate.Configuration):
    def get_context(self, project_name, template_name=None):
        ctx = super(Configuration, self).get_context(project_name, template_name)
        ctx.update(PROJECT_NAME=project_name.upper())
        return ctx

conf = Configuration(__file__)
