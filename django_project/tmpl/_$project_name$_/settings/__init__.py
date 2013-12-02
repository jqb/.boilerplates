# -*- coding: utf-8 -*-
import os
import confy


confy = confy.loader(__file__)


confy.define_module(__name__, [
    confy.from_modules('common', os.environ.get('DJANGO_ENV', 'dev')),
    confy.from_modules('local_settings', silent=True),
])


def apps_from(folder, include_name=True, as_list=False):
    """
    Get all names of django-apps in the project in the given directory/module
    Assuming you have only "core" app in "app" directory::

       INSTALLED_APPS = (
           'django.contrib.admin',
       ) + apps_from('app')

       assert INSTALLED_APPS == ('django.contrib.admin', 'app.core')  # => True

    Or if you have "app" folder on the path you can always do this::

       INSTALLED_APPS = (
           'django.contrib.admin',
       ) + apps_from('app', include_name=False)

       assert INSTALLED_APPS == ('django.contrib.admin', 'core')  # => True
    """
    from os.path import join, abspath, exists

    modules = []
    for dname in os.listdir(folder):
        if exists(abspath(join(folder, dname, '__init__.py'))):
            if include_name:
                name = "%s.%s" % (folder, dname)
            else:
                name = "%s" % (dname)
            modules.append(name)

    if as_list:
        return modules

    return tuple(modules)
