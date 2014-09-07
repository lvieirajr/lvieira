# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

import json
from flask import Blueprint, redirect, render_template, request
from flask.ext.login import login_required, login_user, logout_user, current_user

from .models import User, Project, Partner
from lvieira.app import login_manager

pai_blueprint = Blueprint('pai', __name__)

__all__ = [
    'pai_blueprint',
]


@login_manager.user_loader
def load_user(_id):
    return User.objects(uuid=_id).first() if _id else None


@pai_blueprint.route('/pai/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.objects(email=request.form['email']).first()

        if user and user.password == request.form['password'] and login_user(user):
            partner = Partner.objects(email=user.email).first()

            if not partner:
                partner = Partner(name=user.name, email=user.email)
                partner.save()

            return redirect('/pai')

    return render_template('pai/login.html')


@pai_blueprint.route('/pai/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect('/pai/login')


@pai_blueprint.route('/pai/', methods=['GET'])
@login_required
def home():
    return render_template('pai/index.html')


@pai_blueprint.route('/pai/projetos/', methods=['GET'])
@login_required
def projects():
    return render_template('pai/projects.html', projects=Project.objects())


@pai_blueprint.route('/pai/projetos/novo', methods=['GET', 'POST'])
@login_required
def add_project():
    if request.method == 'POST':
        data = request.form

        Project(name=data['name'], partners=[current_user.email] + data.getlist('partners')).save()

        return projects()
    else:
        return render_template(
            'pai/add_project.html',
            partners=json.dumps([[p.name, p.email] for p in Partner.objects() if p.email != current_user.email]),
        )
