def dodaj_do_rownania(rownanie, wartosci, x):
    wartosc = int(wartosci.pop(0))
    wynik = rownanie * x + wartosc
    if len(wartosci) == 0:
        print("Wynik wielomianu to:")
        print(wynik)
        # return wynik
    else:
        dodaj_do_rownania(wynik, wartosci, x)


def main():
    wartosci = []
    print("Podaj niewiadomą x.")
    x = int(input("> "))
    print("Podaj stopień wielomianu.")
    stopien = int(input("> "))
    stopien = stopien + 1

    for liczbaPetli in range(0, stopien):
        print("Podaj wartość kolejnego składnika wielomianu (od najwyższego stopnia).")
        y = int(input("> "))
        wartosci.append(y)

    dodaj_do_rownania(0, wartosci, x)


main()