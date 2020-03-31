#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, session
from main.middlewares import session_false, session_language
from main.constants import CONSTANTS
from demo.contents.titles import titles
from demo.helpers import index_css, index_js

view = Blueprint('demo_view', __name__)


@view.route('/demo', methods=['GET'])
@session_false
def index():
    lang = session_language(session)
    locals_dic = {
        'title': titles[lang]['index'],
        'message': '',
        'constants': CONSTANTS,
        'csss': index_css(),
        'jss': index_js(),
    }
    return render_template(
      'demo/index.html', 
      locals=locals_dic
    )
