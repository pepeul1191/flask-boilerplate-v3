#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from flask import Flask, redirect, request
from .blueprints import register
from .constants import CONSTANTS
from .templates import load_css, load_js


APP = Flask(
    __name__,
    template_folder='../templates',
    static_folder='../static',
    static_url_path='/static'
)
# blueprints
register(APP)
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


# una ruta de errorhandler
@APP.errorhandler(404)
def not_found():
    if request.method == 'GET':
        extensions_to_check = ['.css', '.js', '.woff', 'png', ]
        if any(ext in request.url for ext in extensions_to_check):
            pass
        else:
            return redirect('/error/access/404')
    else:
        error = {
            'tipo_mensaje': 'error',
            'mensaje': [
                'Recurso no disponible',
                'Error 404'
            ],
        }
        return json.dumps(error), 404


# setear cabeceras
@APP.after_request
def apply_caching(response):
    response.headers['Server'] = 'Werkzeug/0.14.1; Python/3.5.2; Ubuntu;'
    return response
