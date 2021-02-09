from flask import render_template, request, redirect, url_for, flash
from app import app, baza
from models import *

@app.route('/')
def index():
    """Strona główna - pobieranie nazwy wojownika"""
    return render_template('index.html')

@app.route('/lista')
def lista():
    """Strona wyświetlająca id, nazwę i przycisk prowadzący do przedmiotów"""
    wojownicy = Wojownicy.query.all()
    if not wojownicy:
        flash('Brak wojownikow w bazie.')
        return redirect(url_for('index'))
    return render_template('szablon_wojownikow.html', wojownicy=wojownicy)

@app.route('/ekwipunek/<int:id>')
def ekwipunek(id):
    """Strona podaje listę  przedmiotami w ekwipunku"""
    wszystkie_przedmioty = Przedmioty.query.filter_by(wojownik_id=id).all()
    return render_template('szablon_ekwipunku.html', przedmioty=wszystkie_przedmioty)