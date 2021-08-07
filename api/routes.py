import os
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from api.db import get_db
import json
import pandas as pd
import datetime


bp = Blueprint('app_pages', __name__, url_prefix='/')

@bp.route('/test', methods=('GET', 'POST'))
def test():
    return json.dumps({'message': 'Bonjour, from flask routes!'})

@bp.route('/test_create', methods=('GET', 'POST'))
def test_create():
    pass

@bp.route('/test_read', methods=('GET', 'POST'))
def test_read():
    pass

@bp.route('/test_update', methods=('GET', 'POST'))
def test_update():
    pass

@bp.route('/test_delete', methods=('GET', 'POST'))
def test_delete():
    pass