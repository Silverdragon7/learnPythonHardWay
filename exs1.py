#skrypt z możliwością wyboru
from sys import argv
skrypt, nazwaBohatera = argv
print(f"Witaj w grze {skrypt}!. Twoja nazwa to {nazwaBohatera}. Czy chcesz kontynuować?(Yes/No)")
a = input("> ")

if a == "Yes":
    print("Wspaniale. Ruszajmy więc po przygodę!")
    print("""
    Rok 1023 II ery
    Godzina 12.00
    Przechadzasz się ulicą tętniącego życiem miasteczka. Nagle ktoś mija cię z biegnąc w przeciwną stronę.
    Decydujesz się za nim podążyć?(Yes/No)
    """)
    b = input("> ")

    if b == "Yes":
        print("""
        Podążasz za człowiekiem bięgnącym coraz wolniej, jakby uważał że zmylił pościg. 
        Skręca w mniej ruchliwą uliczkę na przedmieściach.
        W końcu zatrzymuje się w jakimś zaułku. Wyglada że cię nie zauważył.
        Stoi do ciebie tyłem i przesuwa palcami po ścianie budynku jakby czegoś szukał.
        Zastanawiasz się czy podejście do niego będzie dobtym pomysłem.
        Może lepiej pozostać w ukryciu.
        Chcesz podejść do nieznajomego?(Yes/No)
        """)
        c = input("> ")
            #ścieżka do zrobienia
        print("""
        Ta ścieżka nie jest jeszcze gotowa... dzięki za przetestowanie dema ;)
        """)

    elif b == "No":
        print("""
        Wzruszasz ramionami i idziesz dalej ulicą jakby nic się nie stało. 
        Po chwili zatrzymuje cię paru strażników, którzy wyglądają jakby kogoś szukali.
        Chcesz im opowiedzieć o człowieku który cię minął?(Yes/No)
        """)
        c = input("> ")

        if c == "Yes":
            print("""
            Wskazujesz strażnikom drogę, a oni ruszają w pościg za nieznajomym.
            Widzisz kątem oka że na dachu coś się poruszyło.
            Wzruszasz ramionami ruszając w stronę domu.
            Otwierasz drzwi i przechodzisz przed próg.
            Nagle czujesz jak coś wbija się w twoje ciało.
            Siły opuszczają twoje ciało a z szyji cieknie krew.
            Przed tobą stoi człowiek podobny do tego który cię mijał.
            Trzyma w ręce małą kuszę z której do ciebie strzelił.
            - Zły wybór - mówi. - Oczy widzą, uszy słyszą, usta milczą.
            Nieznajomy wychodzi podczas gdy umierasz na podłodze swojego pokoju.
            """)
            print("Koniec gry")

        elif c == "No":
            print("""
            Ta ścieżka nie jest jeszcze gotowa... dzięki za przetestowanie dema ;)
            """)
            #wątek drugi

        else:
            print("Wybrano odpowiedź z poza zakresu.")
            print("Koniec gry")


    else:
        print("Wybrano odpowiedź z poza zakresu.")
        print("Koniec gry")

elif a == "No":
    print("Żegnaj")

else:
    print("Wybrano odpowiedź z poza zakresu.")
    print("Koniec gry")