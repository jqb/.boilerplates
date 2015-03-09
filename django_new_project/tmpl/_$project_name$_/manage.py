#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import site
import dotenv; dotenv.read_dotenv()


def setup(root=None, settings_module_name=None):
    """
    Simple setup snippet that makes easy to create
    fast sandbox to try new things.

    :param root: the root of your project
    :param settings_module_name: name of settings module eg:
         "project.setting"

    Usage:
    >>> import manage
    >>> manage.setup()
    >>> # from now on paths are setup, and django is configured
    >>> # you can use it in separate "sandbox" script just to check
    >>> # things really quick
    """
    root = os.path.dirname(os.path.abspath(root or __file__))
    path = lambda *a: os.path.join(root, *a)
    site.addsitedir(path('src'))


if __name__ == "__main__":
    setup()

    from django.core.management import ManagementUtility
    utility = ManagementUtility(None)
    utility.execute()
