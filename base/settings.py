#coding=utf-8
__author__ = 'kevin'

import sys
import os.path

import importlib

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, "site-packages"))


def load_settings(*modules):
    for module in modules:
        try:
            importlib.import_module('%s.settings' % module)
        except ImportError, err:
            raise ImportError("Could not import settings '%s' (Is it on sys.path?): %s" % (module, err))