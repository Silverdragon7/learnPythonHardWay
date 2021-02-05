#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

# utworzenie połączenia z bazą przechowywaną na dysju
# lub w pamięci (':memory:')
# con = sqlite3.connect('test.db')

# dostęp do kolumn przez indeksy i przez nazwy
# con.row_factory = sqlite3.Row

# utworzenie obiektu kursora
# cur = con.cursor()

# tworzenie tabel
# cur.execute("DROP TABLE IF EXISTS klasa;")
#
# cur.execute("""
#     CREATE TABLE IF NOT EXISTS klasa (
#         id INTEGER PRIMARY KEY ASC,
#         nazwa varchar(250) NOT NULL,
#         profil varchar(250) DEFAULT ''
#     )""")

# cur.executescript("""
#     DROP TABLE IF EXISTS uczen;
#     CREATE TABLE IF NOT EXISTS uczen (
#         id INTEGER PRIMARY KEY ASC“klasy,
#         imie varchar(250) NOT NULL,
#         nazwisko varchar(250) NOT NULL,
#         klasa_id INTEGER NOT NULL,
#         FOREIGN KEY(klasa_id) REFERENCES klasa(id)
#     )""")

# wstawiamy jeden rekord danych
# cur.execute('INSERT INTO klasa VALUES(NULL, ?, ?);', ('1A', 'matematyczny'))
# cur.execute('INSERT INTO klasa VALUES(NULL, ?, ?);', ('1B', 'humanistyczny'))


# wykonujemy zapytanie SQL, które pobierze id klasy "1A" z tabeli "klasa".
# cur.execute('SELECT id FROM klasa WHERE nazwa = ?', ('1A',))
# klasa_id = cur.fetchone()[0]

# tupla "uczniowie" zawiera tuple z danymi poszczególnych uczniów
# uczniowie = (
#     (None, 'Tomasz', 'Nowak', klasa_id),
#     (None, 'Jan', 'Kos', klasa_id),
#     (None, 'Piotr', 'Kowalski', klasa_id)
# )

# wstawiamy wiele rekordów
# cur.executemany('INSERT INTO uczen VALUES(?,?,?,?)', uczniowie)

# zatwierdzamy zmiany w bazie
# con.commit()


# pobieranie danych z bazy
# def czytajdane():
#     """Funkcja pobiera i wyświetla dane z bazy."""
#     cur.execute(
#         """
#         SELECT uczen.id,imie,nazwisko,nazwa FROM uczen,klasa
#         WHERE uczen.klasa_id=klasa.id
#         """)
#     uczniowie = cur.fetchall()
#     for uczen in uczniowie:
#         print(uczen['id'], uczen['imie'], uczen['nazwisko'], uczen['nazwa'])
#     print()
#

# czytajdane()

# zmiana klasy ucznia o identyfikatorze 2
# cur.execute('SELECT id FROM klasa WHERE nazwa = ?', ('1B',))
# klasa_id = cur.fetchone()[0]
# cur.execute('UPDATE uczen SET klasa_id=? WHERE id=?', (klasa_id, 2))
#
# # usunięcie ucznia o identyfikatorze 3
# cur.execute('DELETE FROM uczen WHERE id=?', (3,))
#
# czytajdane()

# pętla main
    # input (123)
    # if 1
        #input
        # kdjrghsdh
#
# def main():
#     print("Wybierz opcję: \n1 - wyświetl \n2 - dodaj \n3 - usuń")
#     akcja = input("> ")

    # if akcja == "1":
    #     cur.execute(
    #         """
    #         SELECT uczen.id,imie,nazwisko,nazwa FROM uczen,klasa
    #         WHERE uczen.klasa_id=klasa.id
    #         """)
    #     uczniowie = cur.fetchall()
    #     for uczen in uczniowie:
    #         print(uczen['id']“klasy, uczen['imie'], uczen['nazwisko'], uczen['nazwa'])
    #         continue

    #
    # elif akcja == "2":
    #     print("Podaj informacje do dodania rekordu: ")
    #     print("Imię:")
    #     imie = input("> ")
    #     print("Nazwisko:")
    #     nazwisko = input("> ")
    #     print("Nazwa klasy:")
    #     idKlasy = input("> ")
    #
    #     cur.execute('SELECT id FROM klasa WHERE nazwa = ?', (idKlasy,))
    #     klasa_id = cur.fetchone()[0]
    #     try:
    #         cur.execute('INSERT INTO uczen VALUES(NULL,?,?,?)', (imie, nazwisko, klasa_id))
    #         con.commit()
    #
    #     except ValueError:
    #         print("Błąd")
    #         pass
#####################################################################################

    # elif akcja == "3":
    #     print("Podaj według jakiego klucza chcesz znaleźć rekord do usunięcia:")
    #     print("Do wyboru: ID, Imię, Nazwisko, ID klasy")
    #     sposob = input("> ")
    #     print("Podaj wartość klucza:")
    #     wartosc = input("> ")
    #
    #     cur.execute(f'DELETE FROM uczen WHERE {sposob}=?', (wartosc,))
    #
    # elif akcja == "4":
    #
    # elif akcja == "q":
    #     exit(

con = sqlite3.connect('test.db')


class BazaDanych(object):

    def __init__(self):
        global con
        con.row_factory = sqlite3.Row
        self.cur = con.cursor()
        self.utworz_tabele_klasa()
        self.utworz_tabele_uczen()

    def utworz_tabele_klasa(self):

        self.cur.execute("DROP TABLE IF EXISTS klasa;")

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS klasa (
                id INTEGER PRIMARY KEY ASC,
                nazwa varchar(250) NOT NULL,
                profil varchar(250) DEFAULT ''
            )""")

    def utworz_tabele_uczen(self):
        self.cur.executescript("""
            DROP TABLE IF EXISTS uczen;
            CREATE TABLE IF NOT EXISTS uczen (
                id INTEGER PRIMARY KEY ASC,
                imie varchar(250) NOT NULL,
                nazwisko varchar(250) NOT NULL,
                klasa_id INTEGER NOT NULL,
                FOREIGN KEY(klasa_id) REFERENCES klasa(id)
            )""")

    def zwroc_kursor(self):
        return self.cur


class Uczen:
    def __init__(self, cur):
        self.cur = cur
        cur.execute('SELECT id FROM klasa WHERE nazwa = ?', ('1A',))
        klasa_id = self.cur.fetchone()[0]
        self.uczniowie = (
            (None, 'Tomasz', 'Nowak', klasa_id),
            (None, 'Jan', 'Kos', klasa_id),
            (None, 'Piotr', 'Kowalski', klasa_id)
        )
        self.zapisz_rekordy_uczen()

    def zapisz_rekordy_uczen(self):
        self.cur.executemany('INSERT INTO uczen VALUES(?,?,?,?)', self.uczniowie)
        global con
        con.commit()

    def wyswietl(self, tabela):
        self.cur.execute(f"SELECT * FROM {type(tabela).__name__}")
        lista = self.cur.fetchall()
        return lista

    def dodaj(self, tabela, wartosci):
        x = len(wartosci)
        pytajniki = ""
        for y in range(0, x):
            pytajniki = pytajniki + ",?"
        try:
            self.cur.execute(f'INSERT INTO {type(tabela).__name__} VALUES(NULL{pytajniki})', wartosci)     # nazwa tabeli
            global con
            con.commit()

        except ValueError:
            print("Błąd")
            pass

    def usuwanie(self, sposob, wartosc):
        self.cur.execute(f'DELETE FROM {type(self).__name__} WHERE {sposob}=?', (wartosc,))    # znowu nazwa tabeli

    def zmiana(self, rekord, wartosc, rekorddozmiany, nowawartosc):
        try:
            print(f"UPDATE {type(self).__name__} SET {rekorddozmiany} = '{nowawartosc}' WHERE {rekord} = {wartosc}")
            self.cur.execute(f"UPDATE {type(self).__name__} SET {rekorddozmiany} = '{nowawartosc}' WHERE {rekord} = {wartosc}")
            global con
            con.commit()
        except ValueError:
            print("Błąd")
            pass


class Klasa:
    def __init__(self, cur):
        self.cur = cur
        self.zapisz_rekordy_klasa()

    def zapisz_rekordy_klasa(self):
        self.cur.execute('INSERT INTO klasa VALUES(NULL, ?, ?);', ('1A', 'matematyczny'))
        self.cur.execute('INSERT INTO klasa VALUES(NULL, ?, ?);', ('1B', 'humanistyczny'))

    def wyswietl(self, tabela):
        self.cur.execute(f"SELECT * FROM {type(tabela).__name__}")
        lista = self.cur.fetchall()
        return lista

    def dodaj(self, tabela, wartosci):
        x = len(wartosci)
        pytajniki = ""
        for y in range(0, x):
            pytajniki = pytajniki + ",?"
        try:
            self.cur.execute(f'INSERT INTO {type(tabela).__name__} VALUES(NULL{pytajniki})', wartosci)  # nazwa tabeli
            global con
            con.commit()
        except ValueError:
            print("Błąd")
            pass

    def usuwanie(self, sposob, wartosc):
        self.cur.execute(f'DELETE FROM {self} WHERE {sposob}=?', (wartosc,))

    def zmiana(self, rekord, wartosc, rekorddozmiany, nowawartosc):
        self.cur.execute(f"UPDATE {type(self).__name__} SET {rekorddozmiany} = '{nowawartosc}' WHERE {rekord} = {wartosc}")
        try:
            global con
            con.commit()
        except ValueError:
            print("Błąd")
            pass


class Kontroler:
    def __init__(self, akcja, tabela):
        self.akcja = akcja
        self.tabela = tabela
        self.akcje()

    def akcje(self):
        if self.akcja == "1":
            rekordy = self.tabela.wyswietl(self.tabela)
            self.wyswietl(rekordy, self.tabela)

        elif self.akcja == "2":
            rekord = []
            print("Podaj liczbę argumentów")
            iloscArgumentow = int(input("> "))
            print("Podaj argumenty")
            for x in range(0, iloscArgumentow):
                rekord.append(input("> "))
            self.tabela.dodaj(self.tabela, rekord)

        elif self.akcja == "3":
            print("Podaj według jakiego klucza chcesz znaleźć rekord do usunięcia:")
            sposob = input("> ")
            print("Podaj wartość klucza:")
            wartosc = input("> ")
            self.tabela.usuwanie(sposob, wartosc)

        elif self.akcja == "4":
            print("Podaj według jakiego klucza chcesz znaleźć rekord do zmiany:")
            rekord = input("> ")
            print("Podaj wartość rekordu:")
            wartosc = input("> ")
            print("Podaj wartość do zmiany:")
            rekorddozmiany = input("> ")
            print("Podaj nową wartość:")
            nowawartosc = input("> ")
            self.tabela.zmiana(rekord, wartosc, rekorddozmiany, nowawartosc)

        elif self.akcja == "q":
            exit(0)

    def wyswietl(self, rekordy, tabela):
        nazwa = type(tabela).__name__
        if nazwa == 'Uczen':
            print('--------------------------------')
            for rekord in rekordy:
                print(str(rekord['id']) + " : " + rekord['imie'] + " " + rekord['nazwisko'] + ", klasa:" + str(rekord['klasa_id']))
            print('--------------------------------')
        elif nazwa == 'Klasa':
            print('--------------------------------')
            for rekord in rekordy:
                print(str(rekord['id']) + " : " + rekord['nazwa'] + ' ' + "profil: " + rekord['profil'])
            print('--------------------------------')


def main():
    print("Wybierz tabelę: ")
    wybrana = input("> ")
    if wybrana == "Klasa":
        print("Wybierz opcję: \n1 - wyświetl \n2 - dodaj \n3 - usuń \n4 - zmień")
        akcja = input("> ")
        Kontroler(akcja, klasa)
    elif wybrana == "Uczen":
        print("Wybierz opcję: \n1 - wyświetl \n2 - dodaj \n3 - usuń \n4 - zmień")
        akcja = input("> ")
        Kontroler(akcja, student)
    elif wybrana == "q":
        exit(0)
    else:
        print("Wybrano odpowiedź z poza zakresu")

baza = BazaDanych()
klasa = Klasa(baza.zwroc_kursor())
student = Uczen(baza.zwroc_kursor())
while __name__ == "__main__":
    main()


# Uczen powinien uzywac kursora przekazengo w momencie tworzenia Ucznia z obiektu Baza danych
# Tak samo powinien byc zaimplementowana klasa Klasa
# Input pownien byc realizowany w main albo w Klasie Konroller
# Print moze zostaw w funkcji main
# 4 Mozliwosc przepisania ucznia do innej klasy