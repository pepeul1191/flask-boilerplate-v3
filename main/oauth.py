#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json
from flask import Blueprint, request, session, redirect
from main.constants import OAUTH, CONSTANTS

view = Blueprint('oauth_view', __name__)


def google(req):
    code = req.args.get('code')
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
    return json.loads(r_user.text)

@view.route('/oauth/callback', methods=['GET'])
def callback():
    origin = request.args.get('origin')
    user_data = None
    if origin == 'google':
        user_data = google(request)
        if user_data['locale'] == 'es':
            session['lang'] = 'sp'
        else:
            session['lang'] = user_data['locale']
        session['email'] = user_data['email']
        session['name'] = user_data['name']
        session['picture'] = user_data['picture']
    # locals_dic = { }
    return redirect('/demo')
