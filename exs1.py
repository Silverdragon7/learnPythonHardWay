from sys import argv
import keyboard #import klawiaury

# zabezpieczenie przed brakiem argumentu startowego
if(len(argv) == 1):
    print("Podaj nazwę bohatera jako pierwszy argument.")
    exit()

# informacje o zmiennych dla kodu
fraza = 1
plik = "1.txt"
escape = 0

#skrypt czytający
def otworz_plik(czytany):
    return open(czytany)

def zczytaj_linie(linia, otwarty_plik):
    return otwarty_plik.readlines()[linia]

def zczytaj_wiecej_lini(linia, ilosci_lini, otwarty_plik):
    text = ""
    linia = linia + 1
    ostatnia_linia = linia + ilosci_lini
    lista_linijek = otwarty_plik.readlines()[linia:ostatnia_linia]
    for zmienna in lista_linijek:
        text += zmienna
    return text

# # wartości licznika i nazwy pliku
# def aktualnyt(fraza):
#     fraza = fraza * 10
#     return fraza
#
# # zmiana wartości licznika i nazwy pliku
# def aktualnyn(fraza):
#     fraza = fraza * 10 + 1
#     return fraza


#funkcja szukająca frazy w pliku i podająca linię
def szukaj(fraza, zrodlo):
    counter = 1
    with open(zrodlo, 'r') as read_obj:
        for line in read_obj:
            if f"#{fraza}" in line:

                return counter
            counter = counter + 1

# skrypt pytający o odpowiedź i czytający odpowiednią linię
def wybor(ans, fraza):
    if ans == "Yes":
        fraza = fraza * 10
        counter = szukaj(fraza, plik)

        poczatek_lini = zczytaj_linie(counter, otworz_plik(plik))
        print(zczytaj_wiecej_lini(counter, int(poczatek_lini), otworz_plik(plik)))
        zakonczenie = zczytaj_linie(counter + int(poczatek_lini) + 1, otworz_plik(plik))
        #print(zakonczenie)
        zakoncz = False
        if zakonczenie == "x\n":
            zakoncz = True
        return fraza, zakoncz

    elif ans == "No":
        fraza = fraza * 10 + 1
        counter = szukaj(fraza, plik)

        poczatek_lini = zczytaj_linie(counter, otworz_plik(plik))
        print(zczytaj_wiecej_lini(counter, int(poczatek_lini), otworz_plik(plik)))

        zakonczenie = zczytaj_linie(counter + int(poczatek_lini) + 1, otworz_plik(plik))
        #print(zakonczenie)
        zakoncz = False
        if zakonczenie == "x\n":
            zakoncz = True
        return fraza, zakoncz

    else:
        print("Wybrano odpowiedź z poza zakresu.")
        exit()



#powitanie
skrypt, nazwaBohatera = argv
print(f"Witaj w grze {skrypt}!. Twoja nazwa to {nazwaBohatera}. Czy chcesz kontynuować?(Yes/No)")
a = input("> ")

if a == "No":
    exit("Żegnaj")

elif a == "Yes":
    print("Wspaniale. Ruszajmy więc po przygodę!")
    # pętla właściwa z możliwością wyjścia z programu

    print(zczytaj_wiecej_lini(1, 3, open(plik)))
    fraza = 1
    while escape == False:
        fraza, escape = wybor(input("Yes/No\n> "), fraza)
        print(escape)
else:
    print("Wybrano odpowiedź z poza zakresu.")
    exit()




#counter to licznik linii a fraza to zerojedynkowy wyznacznik szukanej części tekstu


# if a == "Yes":
#
#     print("""
#     \rRok 1023 II ery
#     \rGodzina 12.00
#     \rPrzechadzasz się ulicą tętniącego życiem miasteczka. Nagle ktoś mija cię z biegnąc w przeciwną stronę.
#     \rDecydujesz się za nim podążyć?(Yes/No)
#     """)
#     b = input("> ")
#
#     if b == "Yes":
#         print("""
#         \rPodążasz za człowiekiem bięgnącym coraz wolniej, jakby uważał że zmylił pościg.
#         \rSkręca w mniej ruchliwą uliczkę na przedmieściach.
#         \rW końcu zatrzymuje się w jakimś zaułku. Wyglada że cię nie zauważył.
#         \rStoi do ciebie tyłem i przesuwa palcami po ścianie budynku jakby czegoś szukał.
#         \rZastanawiasz się czy podejście do niego będzie dobtym pomysłem.
#         \rMoże lepiej pozostać w ukryciu.
#         \rChcesz podejść do nieznajomego?(Yes/No)
#         """)
#         c = input("> ")
#             #ścieżka do zrobienia
#         print("""
#         \rTa ścieżka nie jest jeszcze gotowa... dzięki za przetestowanie dema ;)
#         """)
#
#     elif b == "No":
#         print("""
#         \rWzruszasz ramionami i idziesz dalej ulicą jakby nic się nie stało.
#         \rPo chwili zatrzymuje cię paru strażników, którzy wyglądają jakby kogoś szukali.
#         \rChcesz im opowiedzieć o człowieku który cię minął?(Yes/No)
#         """)
#         c = input("> ")
#
#         if c == "Yes":
#             print("""
#             \rWskazujesz strażnikom drogę, a oni ruszają w pościg za nieznajomym.
#             \rWidzisz kątem oka że na dachu coś się poruszyło.
#             \rWzruszasz ramionami ruszając w stronę domu.
#             \rOtwierasz drzwi i przechodzisz przed próg.
#             \rNagle czujesz jak coś wbija się w twoje ciało.
#             \rSiły opuszczają twoje ciało a z szyji cieknie krew.
#             \rPrzed tobą stoi człowiek podobny do tego który cię mijał.
#             \rTrzyma w ręce małą kuszę z której do ciebie strzelił.
#             \r- Zły wybór - mówi. - Oczy widzą, uszy słyszą, usta milczą.
#             \rNieznajomy wychodzi podczas gdy umierasz na podłodze swojego pokoju.
#             """)
#             print("Koniec gry")
#
#         elif c == "No":
#             print("""
#             \rTa ścieżka nie jest jeszcze gotowa... dzięki za przetestowanie dema ;)
#             """)
#             #wątek drugi
#
#         else:
#             print("\rWybrano odpowiedź z poza zakresu.")
#             print("Koniec gry")
#
#
#     else:
#         print("\rWybrano odpowiedź z poza zakresu.")
#         print("Koniec gry")
#
# elif a == "No":
#     print("Żegnaj")
#
# else:
#     print("\rWybrano odpowiedź z poza zakresu.")
#     print("Koniec gry")
