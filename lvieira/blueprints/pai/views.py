# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

import json
from flask import Blueprint, redirect, render_template, request
from flask.ext.login import login_required, logout_user, current_user

from .models import User, Project, Partner
from .controllers import (
    login_controller,
    new_project_controller,
    new_partner_controller,
)
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
    return redirect('/pai/') if login_controller(request) else render_template('/pai/login.html')


@pai_blueprint.route('/pai/logout', methods=['GET'])
@login_required
def logout():
    return redirect('/pai/login') if logout_user() else redirect('/pai/')


@pai_blueprint.route('/pai/', methods=['GET'])
@login_required
def home():
    return render_template('pai/index.html')


@pai_blueprint.route('/pai/projetos/', methods=['GET'])
@login_required
def projects():
    return render_template('pai/projects/index.html', projects=Project.objects())

@pai_blueprint.route('/pai/projetos/<id>', methods=['GET'])
@login_required
def project(id):
    return render_template('pai/projects/project.html', project=Project.objects(id=id).first())


@pai_blueprint.route('/pai/projetos/novo', methods=['GET', 'POST'])
@login_required
def new_project():
    created = new_project_controller(request)

    if created:
        return projects()
    else:
        partners = json.dumps([
            [p.name, p.email] for p in Partner.objects()
            if p.email != current_user.email
        ])

        if created is None:
            return render_template(
                'pai/projects/new.html',
                partners=partners,
                message='Projeto já existe'
            )
        else:
            return render_template('pai/projects/new.html', partners=partners)


@pai_blueprint.route('/pai/socios/', methods=['GET'])
@login_required
def partners():
    return render_template('pai/partners/index.html', partners=Partner.objects())


@pai_blueprint.route('/pai/socios/<id>', methods=['GET'])
@login_required
def partner(id):
    return render_template('pai/partners/partner.html', partner=Partner.objects(id=id).first())


@pai_blueprint.route('/pai/socios/novo', methods=['GET', 'POST'])
@login_required
def new_partner():
    created = new_partner_controller(request)

    if created:
        return partners()
    else:
        if created is None:
            return render_template(
                'pai/partners/new.html',
                message='Projeto já existe'
            )
        else:
            return render_template('pai/partners/new.html')
