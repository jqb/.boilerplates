# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import _$project_name$_


setup(
    name='_$project_name$_',
    version=_$project_name$_.VERSION,
    description='',
    author='_$author$_',
    author_email='_$email$_',
    include_package_data=True,
    url='https://github.com/_$github_profile$_/_$project_name$_/tree/ver-%s' % _$project_name$_.VERSION,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)

# Usage of setup.py:
# $> python setup.py register             # registering package on PYPI
# $> python setup.py build sdist upload   # build, make source dist and upload to PYPI
