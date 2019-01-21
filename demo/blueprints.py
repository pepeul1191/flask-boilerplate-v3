#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .views import demo_view
from .apis.demo import demo_api

blueprints = [
    demo_view,
    demo_api,
]
