#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from flask import Blueprint


demo_api = Blueprint('demo_api', __name__)


@demo_api.route('/demo/api', methods=['GET'])
# @session_false
def index():
    rpta = None
    status = 200
    try:
        rpta = {
            'mensaje': '=)'
        }
    except Exception as e:
        rpta = {
            'tipo_mensaje': 'error',
            'mensaje': [
                'Se ha producido un error en listar las provincias del '
                + 'departamento',
                str(e)
            ],
        }
        status = 500
    return json.dumps(rpta), status
