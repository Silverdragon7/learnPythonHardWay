import random
from sys import argv

class Karta:
    def __init__(self):
        self.kolor = None
        self.wartosc = None
        self.wartosc_bojowa = None
        self.losuj_kolor()
        self.losowanie_karty()
        self.zamiana_znaku_na_wartosc()
        self.ustaw_wartosc_bojowa()

    def losuj_kolor(self):
        kolory = ["Serce", "Dzwonek", "Trefl", "Wino"]
        losowa2 = random.randint(0, 3)
        kolor_karty = kolory[losowa2]
        self.kolor = kolor_karty

    def losowanie_karty(self):
        talia = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        losowa = random.randint(0, 12)
        numer_karty = talia[losowa]
        self.wartosc = numer_karty

    def zamiana_znaku_na_wartosc(self):
        if self.wartosc == "J":
            self.wartosc_bojowa = 11
        elif self.wartosc == "Q":
            self.wartosc_bojowa = 12
        elif self.wartosc == "K":
            self.wartosc_bojowa = 13
        elif self.wartosc == "A":
            self.wartosc_bojowa = 14
        else:
            self.wartosc_bojowa = self.wartosc

    def ustaw_wartosc_bojowa(self):
        if self.kolor == "Serce":
            self.wartosc_bojowa = float(self.wartosc_bojowa) + 0.75

        elif self.kolor == "Dzwonek":
            self.wartosc_bojowa = float(self.wartosc_bojowa) + 0.5

        elif self.kolor == "Wino":
            self.wartosc_bojowa = float(self.wartosc_bojowa) + 0.25

        else:
            self.wartosc_bojowa = float(self.wartosc_bojowa)

    def pokaz_wartosc_bojowa(self):
        return self.wartosc_bojowa

    def pokaz_kolor(self):
        return self.kolor

    def pokaz_wartosc(self):
        return self.wartosc


class Gracz:
    def __init__(self):
        self.karty = []
        self.oznaczenia_kart = []
        self.wartosci = []
        self.najwyzsza_wartosc = None
        self.najwyzsza_karta = None
        self.podaj_karty()
        self.wybierz_najwyzsza()
        self.usun_najwyzsza()

    def podaj_karty(self):
        for x in range(0, 5):
            y = Karta()
            self.karty.append(y)

    def wybierz_najwyzsza(self):
        for aktualna_karta in self.karty:
            self.wartosci.append(Karta.pokaz_wartosc_bojowa(aktualna_karta))
        self.wartosci.sort()
        self.najwyzsza_wartosc = self.wartosci[-1] #DODAĆ WYBIERANIE NAJWIĘKSZEJ KARTY NIE WARTOŚCI
        self.karty.sort(key=lambda x: getattr(x, "wartosc_bojowa"))
        self.najwyzsza_karta = self.karty[-1]

    def pokaz_karty(self):
        for karta in self.karty:
            self.oznaczenia_kart.append({karta.pokaz_wartosc():karta.pokaz_kolor()})
        return self.oznaczenia_kart # POPRAWIĆ

    def pokaz_najwyzsza(self):
        return (self.najwyzsza_karta).pokaz_wartosc() + " " + (self.najwyzsza_karta).pokaz_kolor()

    def pokaz_najwyzsza_wartosc(self):
        return self.najwyzsza_wartosc

    def usun_najwyzsza(self):
        self.karty.pop()
        self.wybierz_najwyzsza()

class Gra:
    def __init__(self, ilosc_graczy):
        self.



def rozgrywka():

    atut1 = player1.pokaz_najwyzsza_wartosc()
    atut2 = player2.pokaz_najwyzsza_wartosc()
    print(atut1)
    print(atut2)
    if atut1 > atut2:
        print("Zwyciężył gracz 1: ", player1.pokaz_najwyzsza())
    elif atut1 < atut2:
        print("Zwyciężył gracz 2: ", player2.pokaz_najwyzsza())
    else:
        print("Remis")

def main():
    global player1
    global player2
    player1 = Gracz()
    player2 = Gracz()
    print("Karty pierwszego gracza: ", player1.pokaz_karty())
    print("Karty drugiego gracza: ", player2.pokaz_karty())
    # print(player1.pokaz_najwyzsza())
    # test = Karta()
    # print(test.pokaz_wartosc())
    # wartosci = (wartosc_karty(zamiana_znaku_na_wartosc(karty1)))
    # wartosci1 = (wartosc_karty(zamiana_znaku_na_wartosc(karty2)))
    rozgrywka()

main()