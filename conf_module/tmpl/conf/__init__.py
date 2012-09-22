# -*- coding: utf-8 -*-
from os import environ
from os.path import dirname, abspath, join, exists, basename


# creating path to configuration directory
config_directory_path = dirname(abspath(__file__))


# # sequence of settings module to read
files_base_names = [
    'default',
    environ.get('_$PROJECT_NAME$__ENV', 'development'),
]


# # load settings here - to the module level
for base_name in files_base_names:
    filepath = '%s/%s.py' % (config_directory_path, base_name)
    if not exists(filepath):
        raise ImportError("Configuration loading error: file '%s' does not exists" % filepath)
    execfile(filepath)


# # module cleanup
del base_name, files_base_names, filepath, config_directory_path


# # import cleanup - we do not want to have those in configuration
del join, dirname, abspath, environ, exists, basename

