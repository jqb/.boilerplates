# -*- coding: utf-8 -*-
from django.test import TestCase


class ImportTest(TestCase):
    def test_import_test(self):
        try:
            import _$project_name$_
        except ImportError:
            self.fail("There were problems with '_$project_name$_' module import")
