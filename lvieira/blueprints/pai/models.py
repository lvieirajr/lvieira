# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

from mongoengine import (
    Document,
    StringField,
    EmailField,
    DateTimeField,
    DecimalField,
    DictField,
    ReferenceField
)
from decimal import Decimal
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


class Land(Document):
    name = StringField()
    address = StringField(required=True)

    width = DecimalField(required=True)
    height = DecimalField(required=True)

    purchase_price = DecimalField(required=True)
    costs = DictField()

    def __unicode__(self):
        if self.name and self.address:
            return self.address + ' (' + self.name + ')'
        else:
            return self.name or self.address or 'Terreno'

    @property
    def size(self):
        if self.width and self.height:
            return Decimal(self.width * self.height)
        else:
            return Decimal('0.0')

    @property
    def cost(self):
        return self.purchase_price + sum(value for key, value in self.costs.items())


class Building(Document):
    name = StringField()
    land = ReferenceField(Land)

    costs = DictField()

    def __unicode__(self):
        if self.name and self.land:
            return self.name + ' no terreno: ' + unicode(self.land)
        elif self.name:
            return self.name
        elif self.land:
            return 'Construção no terreno: ' + unicode(self.land)
        else:
            return 'Construção'

    @property
    def cost(self):
        return sum(value for key, value in self.costs.items())
