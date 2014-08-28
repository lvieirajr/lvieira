# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

from flask import Blueprint, redirect, render_template, request
from flask.ext.login import login_required, login_user, logout_user

from .models import User
from lvieira.app import login_manager

pai_blueprint = Blueprint('pai', __name__)

__all__ = [
    'pai_blueprint',
]


@login_manager.user_loader
def load_user(_id):
    return User.objects(uuid=_id).first() if _id else None


@pai_blueprint.route('/pai/login', methods=['GET'])
def login():
    if request.method == 'POST':
        user = User.objects(email=request.form['email']).first()

        if user and user.password == request.form['password'] and login_user(user):
            return redirect('/pai')

    return render_template('pai/login.html')


@pai_blueprint.route('/pai/', methods=['GET'])
@login_required
def home():
    return render_template('pai/index.html')


@pai_blueprint.route('/pai/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect('/pai/login')



