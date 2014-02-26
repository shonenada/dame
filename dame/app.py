#/usr/bin/env python
#-*- coding: utf-8 -*-

from framework import BaseFramework


class Dame(BaseFramework):

    def __init__(self, import_name, **kwargs):
        BaseFramework.__init__(self, import_name, **kwargs)
