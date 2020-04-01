#!/usr/bin/env python
# -*- coding: utf-8 -*-

from demo.blueprints import blueprints as demo_blueprints
from .error import view as error_view
from .oauth import view as oauth_view

def register(app):
    modules_blueprints = []
    # registrar blueprint of apps
    modules_blueprints.append(demo_blueprints)
    # cargar blueprints a app
    for blueprints in modules_blueprints:
        for blueprint in blueprints:
            app.register_blueprint(blueprint)
    # registrar oauth
    app.register_blueprint(oauth_view)
    # registar error/access/:code
    app.register_blueprint(error_view)
