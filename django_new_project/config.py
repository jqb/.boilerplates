# -*- coding: utf-8 -*-
import subprocess
from random import choice

from boilerplate import Configuration, ProjectCreator as PC


class ProjectCreator(PC):
    def after_file_create(self, destination_file_path):
        if destination_file_path.endswith('manage.py'):
            subprocess.call(['chmod', '+x', destination_file_path])


conf = Configuration(__file__, {
    'secret_key': ''.join([
        choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)
    ]),
    'django_version': '1.6',
}, creator_class=ProjectCreator)
