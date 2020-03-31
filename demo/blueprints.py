#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .views.index import view as demo_view
from .apis.demo import api as demo_api

blueprints = [
    demo_view,
    demo_api,
]
