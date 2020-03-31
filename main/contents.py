# !/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml


def get_yaml(module, file):
    file_route = module + '/contents/' +  file + '.yml'
    content = None
    with open(file_route , 'r') as file:
        content = yaml.full_load(file)
    return content
        