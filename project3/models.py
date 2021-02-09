# -*- coding: utf-8 -*-
# quiz-orm/models.py
from app import baza


class Wojownicy(baza.Model):
    __tablename__ = 'wojownicy'
    id = baza.Column(baza.Integer, primary_key=True)
    nazwa = baza.Column(baza.Unicode(255), unique=True)
    przedmioty = baza.relationship("Przedmioty", back_populates="wojownicy")

    def __str__(self):
        return self.nazwa


class Przedmioty(baza.Model):
    __tablename__ = 'przedmioty'
    id = baza.Column(baza.Integer, primary_key=True)
    nazwa_przedmiotu = baza.Column(baza.Unicode(255))
    opis = baza.Column(baza.Unicode(100))
    wojownik_id = baza.Column(baza.Integer, baza.ForeignKey('wojownicy.id'))
    wojownicy = baza.relationship("Wojownicy", back_populates="przedmioty",
# 'Wojownik', backref=baza.backref('nazwa'),
        cascade="all, delete")

    def __str__(self):
        return self.nazwa_przedmiotu