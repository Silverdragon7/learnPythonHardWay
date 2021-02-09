# -*- coding: utf-8 -*-
# quiz-orm/models.py

from peewee import *
from app import baza


class BaseModel(Model):
    class Meta:
        database = baza


class Pytanie(BaseModel):
    pytanie = CharField()
    odpok = CharField()

    def __str__(self):
        return self.pytanie


class Odpowiedz(BaseModel):
    pnr = ForeignKeyField(
        Pytanie, backref='odpowiedzi', on_delete='CASCADE', primary_key=True)
    odpowiedz = CharField()

    def __str__(self):
        return self.odpowiedz