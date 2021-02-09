# -*- coding: utf-8 -*-
# quiz-pw/dane.py

import os
import csv
from models import Przedmioty, Wojownicy
from app import baza
import sqlite3
import sys

def pobierz_dane(plikcsv):
    """Funkcja zwraca tuplę zawierającą tuple z danymi z pliku csv."""
    dane = []
    if os.path.isfile(plikcsv):
        with open(plikcsv, newline='') as plikcsv:
            tresc = csv.reader(plikcsv, delimiter='#')
            for rekord in tresc:
                dane.append(tuple(rekord))
    else:
        print("Plik z przedmiotami", plikcsv, "nie istnieje!")
    return tuple(dane)


def dodaj_przedmiot(dane):
    for nazwa, opis, wlasciciel in dane:
        n = Przedmioty(nazwa_przedmiotu=nazwa, opis=opis, wojownik_id=wlasciciel)
        baza.session.add(n)
        baza.session.commit()
        # for o in odpowiedzi.split(","):
        #     odp = Odpowiedz(pnr=p.id, odpowiedz=o.strip())
        #     baza.session.add(odp)
        # baza.session.commit()
    print("Dodano przedmiot")


def dodaj_wojownika(dane):
    # dane = dane.strip("()")
    for wojownik in dane:
        w = Wojownicy(nazwa=wojownik[0])
        baza.session.add(w)
        baza.session.commit()
    print("Dodano wojownika")
