# -*- coding: utf-8 -*-
# Helper file to be loaded via both manage.py and settings
import dotenv
import dj_database_url  # NOQA
from getenv import env  # NOQA


def project_path(thefile, *args):
    from os.path import join, dirname, abspath
    root = abspath(join(dirname(abspath(thefile)), *args))
    return lambda *a: join(root, *a)
project_path = project_path(__file__, '..')  # pointing to repo root


dotenv.read_dotenv(project_path('.env'))
