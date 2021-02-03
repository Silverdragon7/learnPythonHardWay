
aktualny_plik = 1


def podaj_kolejny_plik(aktualny_plik, argument):
    if argument == "tak":
        nastepny_plik = aktualny_plik * 10
    elif argument == "nie":
        nastepny_plik = aktualny_plik * 10 + 1
    else:
        nastepny_plik = aktualny_plik
    return nastepny_plik


def przeczytaj_plik(sciezka):
    x = open(sciezka, 'r')
    return x.read()


def main(argument):
    global aktualny_plik
    aktualny_plik = podaj_kolejny_plik(aktualny_plik, argument)
    czytany = aktualny_plik
    czytany2 = "docs/" + str(czytany) + ".txt"
    return przeczytaj_plik(czytany2)

#
# while True:
#     odp = input()
#     print(main(odp))

# program nie zwraca pliku nr 1
# musi po podaniu odpowiedzi przejść do kolejnych