# -*- coding: utf-8 -*-
# quiz-orm/app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# konfiguracja aplikacji
app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
    DATABASE=os.path.join(app.root_path, 'ekwipunek.db'),
    SQLALCHEMY_DATABASE_URI='sqlite:///' +
                            os.path.join(app.root_path, 'ekwipunek.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    TYTUL='Ekwipunek bohatera'
))

# tworzymy instancję bazy używanej przez modele
baza = SQLAlchemy(app)
