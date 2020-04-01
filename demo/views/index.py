#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, session
from main.middlewares import session_false, session_language
from main.constants import CONSTANTS
from main.contents import get_yaml
from demo.helpers import index_css, index_js

view = Blueprint('demo_view', __name__)


@view.route('/demo', methods=['GET'])
@session_false
def index():
    lang = session_language(session)
    titles = get_yaml('demo', 'titles')
    url_google = 'https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id=1044701093820-jam7g5carn4nghkkhqr75ustq0l5vrum.apps.googleusercontent.com&redirect_uri=' + CONSTANTS['base_url'] + 'oauth/callback?origin=google&scope=profile email'
    locals_dic = {
        'title': titles['index'][lang]['index'],
        'message': '',
        'constants': CONSTANTS,
        'csss': index_css(),
        'jss': index_js(),
        'url_google': url_google,
    }
    return render_template(
      'demo/index.html', 
      locals=locals_dic
    )
