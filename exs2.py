import random
#
#
# def wylosuj_karte():
#     talia = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
#
#     numer = random.randint(0, 12)
#     return(talia[numer])
#
# def wylosuj_5_kart():
#     karty_gracza = []
#     wartosci_kart = []
#     for x in range(0, 5):
#         karty_gracza.append(wylosuj_karte())
#     wartosci_kart = karty_gracza
#     return karty_gracza, wartosci_kart
#
# def wysokosc_karty(karty):
#     wysokosci = []
#     for karta in karty:
#         if karta == "J":
#              wysokosci.append(11)
#         elif karta == "Q":
#             wysokosci.append(12)
#         elif karta == "K":
#             wysokosci.append(13)
#         elif karta == "A":
#             wysokosci.append(14)
#         else:
#             wysokosci.append(int(karta))
#     return wysokosci
#
# def oznaczenie_karty(karta):
#     if karta == 11:
#         return "J"
#     elif karta == 12:
#         return "Q"
#     elif karta == 13:
#         return "K"
#     elif karta == 14:
#         return "A"
#     else:
#         return karta
#
# def najwyzsza_karta(karty):
#     karty.sort()
#     nk = karty[-1]
#     return nk
#
# def rozgrywka(wartosci1, wartosci2):
#     atut1 = najwyzsza_karta(wysokosc_karty(wartosci1))
#     atut2 = najwyzsza_karta(wysokosc_karty(wartosci2))
#
#
#     if atut1 > atut2:
#         print("Zwyciężył gracz 1: ", oznaczenie_karty(atut1))
#     elif atut1 < atut2:
#         print("Zwyciężył gracz 2: ", oznaczenie_karty(atut2))
#     else:
#         wartosci1.sort()
#         wartosci2.sort()
#         wartosci1.pop()
#         wartosci2.pop()
#         rozgrywka(wartosci1, wartosci2)
#
#
#
# def main():
#     gracz1, wartosci1 = wylosuj_5_kart()
#     gracz2, wartosci2 = wylosuj_5_kart()
#     print("Karty pierwszego gracza: ", " ".join(gracz1), "Karty drugiego gracza: ", " ".join(gracz2))
#     rozgrywka(wartosci1, wartosci2)
#
# main()

# basic
def losowanie_karty():
    talia = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    #kolory = ["Kier", "Karo", "Trefl", "Pik"]
    losowa = random.randint(0, 12)
    #losowa2 = random.randint(0, 3)
    #return (talia[numer])
    numer_karty = talia[losowa]
    #kolor_karty = kolory[losowa2]
    #karta = {numer_karty:kolor_karty}

    return numer_karty

def losowanie_koloru():
    kolory = ["Serce", "Dzwonek", "Trefl", "Wino"]
    losowa2 = random.randint(0, 3)
    kolor_karty = kolory[losowa2]
    return kolor_karty


#podaje karty
def losowanie_5_kart_z_kolorami():

    karty_gracza = []
    for x in range(0, 5):
        karta = losowanie_karty()
        kolor =  losowanie_koloru()
        karty_gracza.append({"Wartosc":karta, "Kolor":kolor})
    return karty_gracza

#zamienia znaki na wartości
def zamiana_znaku_na_wartosc(karty):
    wartosci = []
    for karta in karty:
        if karta["Wartosc"] == "J":
             karta["Wartosc"] = 11
             wartosci.append(karta)
        elif karta["Wartosc"] == "Q":
             karta["Wartosc"] = 12
             wartosci.append(karta)
        elif karta["Wartosc"] == "K":
             karta["Wartosc"] = 13
             wartosci.append(karta)
        elif karta["Wartosc"] == "A":
             karta["Wartosc"] = 14
             wartosci.append(karta)
        else:
            wartosci.append(karta)
    return wartosci

#sumuje wartości dla poszczególnych kolorów
def wartosc_karty(karty):
    wartosci = []
    for karta in karty:

    #wartość karty po dodaniu koloru
        if karta["Kolor"] == "Serce":
            karta["Wartosc"] = float(karta["Wartosc"]) + 0.75
            wartosci.append(karta["Wartosc"])

        elif karta["Kolor"] == "Dzwonek":
            karta["Wartosc"] = float(karta["Wartosc"]) + 0.5
            wartosci.append(karta["Wartosc"])

        elif karta["Kolor"] == "Wino":
            karta["Wartosc"] = float(karta["Wartosc"]) + 0.25
            wartosci.append(karta["Wartosc"])

        else:
            wartosci.append(float(karta["Wartosc"]))
    return wartosci




def najwyzsza_karta(karty):
    karty.sort()
    nk = karty[-1]
    return nk

def rozgrywka(wartosci, wartosci1):
    # wartosci = (wartosc_karty(zamiana_znaku_na_wartosc(karty1)))
    # wartosci1 = (wartosc_karty(zamiana_znaku_na_wartosc(karty2)))

    atut1 = (najwyzsza_karta(wartosci))
    atut2 = (najwyzsza_karta(wartosci1))
    if atut1 > atut2:
        print("Zwyciężył gracz 1: ", najwyzsza_karta(wartosci))
    elif atut1 < atut2:
        print("Zwyciężył gracz 2: ", najwyzsza_karta(wartosci1))
    else:
        wartosci.sort()
        wartosci1.sort()
        wartosci.pop()
        wartosci1.pop()
        rozgrywka(wartosci, wartosci1)

def main():
    karty1 = losowanie_5_kart_z_kolorami()
    karty2 = losowanie_5_kart_z_kolorami()
    print("Karty pierwszego gracza: ", karty1)
    print("Karty drugiego gracza: ", karty2)
    wartosci = (wartosc_karty(zamiana_znaku_na_wartosc(karty1)))
    wartosci1 = (wartosc_karty(zamiana_znaku_na_wartosc(karty2)))
    rozgrywka(wartosci, wartosci1)

main()