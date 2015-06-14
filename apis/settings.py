#coding=utf-8
__author__ = 'kevin'

import os
import os.path

def load_tornado_settings(path):
    return {
       "template_path": os.path.join(path, "views"),
        "static_path": os.path.join(path, "views"),
    }