import random
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