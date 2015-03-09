# -*- coding: utf-8 -*-
import os

def create_projectpath(thefile):
    from os.path import join, dirname, abspath
    root = abspath(join(dirname(abspath(thefile)), '..'))
    return lambda *a: join(root, *a)

# "Temporary globals" that migth be useful
# It can be used in each settings file as builtin
projectpath = create_projectpath(__file__)


def apps_from(folder, include_name=False, as_list=False):
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
