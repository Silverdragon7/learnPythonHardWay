import random


def wylosuj_karte():
    talia = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    numer = random.randint(0, 12)
    return(talia[numer])

def wylosuj_5_kart():
    karty_gracza = []
    wartosci_kart = []
    for x in range(0, 5):
        karty_gracza.append(wylosuj_karte())
    wartosci_kart = karty_gracza
    return karty_gracza, wartosci_kart

def wysokosc_karty(karty):
    wysokosci = []
    for karta in karty:
        if karta == "J":
             wysokosci.append(11)
        elif karta == "Q":
            wysokosci.append(12)
        elif karta == "K":
            wysokosci.append(13)
        elif karta == "A":
            wysokosci.append(14)
        else:
            wysokosci.append(int(karta))
    return wysokosci

def oznaczenie_karty(karta):
    if karta == 11:
        return "J"
    elif karta == 12:
        return "Q"
    elif karta == 13:
        return "K"
    elif karta == 14:
        return "A"
    else:
        return karta

def najwyzsza_karta(karty):
    karty.sort()
    nk = karty[-1]
    return nk

def rozgrywka(wartosci1, wartosci2):
    atut1 = najwyzsza_karta(wysokosc_karty(wartosci1))
    atut2 = najwyzsza_karta(wysokosc_karty(wartosci2))


    if atut1 > atut2:
        print("Zwyciężył gracz 1: ", oznaczenie_karty(atut1))
    elif atut1 < atut2:
        print("Zwyciężył gracz 2: ", oznaczenie_karty(atut2))
    else:
        wartosci1.sort()
        wartosci2.sort()
        wartosci1.pop()
        wartosci2.pop()
        rozgrywka(wartosci1, wartosci2)



def main():
    gracz1, wartosci1 = wylosuj_5_kart()
    gracz2, wartosci2 = wylosuj_5_kart()
    print("Karty pierwszego gracza: ", " ".join(gracz1), "Karty drugiego gracza: ", " ".join(gracz2))
    rozgrywka(wartosci1, wartosci2)

main()