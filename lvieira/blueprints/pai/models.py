# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

from mongoengine import Document, StringField, EmailField, DateTimeField
from uuid import uuid4
from datetime import datetime

__all__ = [
    'User',
]


class User(Document):
    name = StringField(required=True)
    email = EmailField(unique=True, required=True)
    password = StringField(required=True)
    uuid = StringField(default=uuid4().get_hex)
    created = DateTimeField(default=datetime.now())

    def __unicode__(self):
        return self.name + ' (' + self.email + ')'

    def get_id(self):
        return self.uuid

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False
