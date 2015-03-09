#!/usr/bin/env python
# -*- coding: utf-8 -*-
import loading  # enough to load settings and .env
from django.core.management import ManagementUtility


if __name__ == "__main__":
    utility = ManagementUtility(None)
    utility.execute()
