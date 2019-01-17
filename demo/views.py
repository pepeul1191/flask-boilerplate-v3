#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from flask import Blueprint, render_template, request, session, redirect
# from main.constants import constants
# from main.middlewares import session_false, session_true
# from .helpers import index_css, index_js

demo_view = Blueprint('demo_view', __name__)

@demo_view.route('/demo', methods=['GET'])
def index():
  return render_template('demo/index.html')
