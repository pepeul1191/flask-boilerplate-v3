#!/usr/bin/env python
# -*- coding: utf-8 -*-
from demo.blueprints import blueprints as demo_blueprints

def register(app):
  modules_blueprints = []
  #registrar blueprint of apps
  modules_blueprints.append(demo_blueprints)
  #cargar blueprints a app
  for blueprints in modules_blueprints:
    for blueprint in blueprints:
      app.register_blueprint(blueprint)
