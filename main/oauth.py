#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from flask import Blueprint, request
from main.constants import OAUTH, CONSTANTS

view = Blueprint('oauth_view', __name__)


@view.route('/oauth/callback', methods=['GET'])
def callback():
    code = request.args.get('code')
    # get oauth google token
    r_oauth = requests.post(
        'https://oauth2.googleapis.com/token',
        data = {
            'client_id': OAUTH['google']['client_id'],
            'client_secret': OAUTH['google']['client_secret'],
            'code': code,
            'grant_type': 'authorization_code',
            'redirect_uri': CONSTANTS['base_url'] + 'oauth/callback?origin=google',
        }
    )
    oauth = json.loads(r_oauth.text)
    # get oauth google user
    r_user = requests.get(
        'https://www.googleapis.com/oauth2/v1/userinfo',
        params = {
            'access_token': oauth['access_token'],
        }
    )
    # user = json.loads(r_user.text)
    print(r_user.text)
    # locals_dic = { }
    # return render_template('demo/index.html', locals=locals_dic)
    return 'Recurso no encontrado', 200
