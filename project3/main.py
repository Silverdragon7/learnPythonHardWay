# -*- coding: utf-8 -*-
# quiz-pw/main.py

import os
from app import app
from flask import Flask
from models import *
from views import *
from dane import dodaj_przedmiot, pobierz_dane, dodaj_wojownika


if __name__ == '__main__':
    if not os.path.exists(app.config['DATABASE']):
        baza.create_all()  # tworzymy tabele
        baza.session.commit()
        dodaj_przedmiot(pobierz_dane('eq.csv'))
        dodaj_wojownika(pobierz_dane('wojownicy.csv'))

    app.run(debug=True)