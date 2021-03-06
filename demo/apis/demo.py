#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from flask import Blueprint


api = Blueprint('demo_api', __name__)


@api.route('/demo/api', methods=['GET'])
# @session_false
def index():
    rpta = None
    status = 200
    try:
        rpta = {
            'mensaje': '=)'
        }
    except TypeError as e:
        rpta = {
            'tipo_mensaje': 'error',
            'mensaje': [
                'Se ha producido un error TypeError en listar los '
                + 'departamentos',
                str(e)
            ],
        }
        status = 500
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
