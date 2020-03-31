#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint

view = Blueprint('error_view', __name__)


@view.route('/error/access/<code>', methods=['GET'])
def access(code):
    # lang = session_language(session)
    # locals_dic = { }
    # return render_template('demo/index.html', locals=locals_dic)
    return 'Recurso no encontrado', code
