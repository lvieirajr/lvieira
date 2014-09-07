# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

from mongoengine import *
from decimal import Decimal
from uuid import uuid4
from datetime import datetime

__all__ = [
    'User',
    'Land',
    'Building',
    'Partner',
    'Project',
]


class User(Document):
    name = StringField(required=True)
    email = EmailField(unique=True, required=True)
    password = StringField(required=True)
    uuid = StringField(default=uuid4().get_hex)
    created = DateTimeField(default=datetime.now())

    def __unicode__(self):
        if self.name and self.email:
            return self.name + ' (' + self.email + ')'
        elif self.name:
            return self.name
        elif self.email:
            return self.email
        else:
            return 'Usuário'

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

    width = DecimalField(required=True, default=Decimal('0.00'))
    height = DecimalField(required=True, default=Decimal('0.00'))

    purchase_price = DecimalField(required=True, default=Decimal('0.00'))
    costs = DictField()

    buildings = ListField()

    def __unicode__(self):
        if self.name and self.address:
            return self.address + ' (' + self.name + ')'
        else:
            return self.name or self.address or 'Terreno'

    @property
    def size(self):
        return Decimal(self.width * self.height)

    @property
    def total_cost(self):
        return self.purchase_price + sum(value for key, value in self.costs.items())

    @property
    def cost_per_building(self):
        return self.total_cost / Decimal(len(self.buildings))


class Building(Document):
    name = StringField()
    costs = DictField()
    land = ReferenceField(Land)

    def __unicode__(self):
        return self.name or 'Construção'

    @property
    def cost(self):
        return sum(value for key, value in self.costs.items())


class Partner(Document):
    name = StringField(required=True)
    email = EmailField(unique=True, required=True)

    def __unicode__(self):
        return self.name or 'Sócio'


class Project(Document):
    name = StringField(unique=True, required=True)
    partners = ListField(required=True)
    lands = ListField(ReferenceField(Land))

    def __unicode__(self):
        return self.name or 'Projeto'
