# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

from flask.ext.login import login_user, current_user

from .models import *

__all__ = [
    'login_controller',
]


def login_controller(request):
    if request.method == 'POST':
        user = User.objects(email=request.form['email']).first()

        if user and user.password == request.form['password'] and login_user(user):
            partner = Partner.objects(email=user.email).first()

            if not partner:
                Partner(name=user.name, email=user.email).save()

            return True

    return False


def new_project_controller(request):
    if request.method == 'POST':
        partner_emails = [current_user.email] + request.form.getlist('partners')
        partner_percents = request.form.getlist('percents')

        partners = []
        for i in range(len(partner_emails)):
            partners.append([partner_emails[i], int(partner_percents[i])])

        try:
            return Project(name=request.form['name'], partners=partners).save()
        except:
            return None

    return False


def new_partner_controller(request):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        try:
            return Partner(name=name, email=email).save()
        except:
            return None

    return False
