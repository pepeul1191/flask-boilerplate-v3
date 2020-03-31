#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from .middlewares import not_found
from .blueprints import register
from .constants import CONSTANTS
from .templates import load_css, load_js


APP = Flask(
    __name__,
    template_folder='../templates',
    static_folder='../static',
    static_url_path='/'
)
# blueprints
register(APP)
# registrer 404 handler
APP.register_error_handler(404, not_found)
# configuración de session
APP.config['SESSION_TYPE'] = 'filesystem'
APP.secret_key = CONSTANTS['key']

# configur de filters/helpers en los templates
@APP.context_processor
def utility_processor():
    return dict(
        load_css=load_css,
        load_js=load_js
    )

# una ruta de prueba
@APP.route('/hello')
def hello_world():
    return 'Hello, World???!'

# setear cabeceras
@APP.after_request
def apply_caching(response):
    response.headers['Server'] = 'Werkzeug/0.14.1; Python/3.5.2; Ubuntu;'
    return response
