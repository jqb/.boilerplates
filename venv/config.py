# -*- coding: utf-8 -*-
import os
import subprocess
import boilerplate


class ProjectCreator(boilerplate.ProjectCreator):
    def after_create(self, destination_path):
        # HACK: I don't have access to context here :(
        venv_name_path = os.path.join(destination_path, '.venv', 'default')
        venv_name = open(venv_name_path, 'r').read().strip('\n')
        venv_path = os.path.join('.venv', venv_name)

        print '    Running virtualenv in %s' % destination_path
        print ''

        subprocess.call(['virtualenv-2.7', venv_path])


conf = boilerplate.Configuration(__file__, {
    # put your context variables here, to use them in your project template
}, creator_class=ProjectCreator)
