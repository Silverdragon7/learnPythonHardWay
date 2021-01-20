from sys import argv

if(len(argv) == 1):
    print("Podaj nazwę bohatera jako pierwszy argument.")
    exit()

skrypt, nazwaBohatera = argv
print(f"Witaj w grze {skrypt}!. Twoja nazwa to {nazwaBohatera}. Czy chcesz kontynuować?(Yes/No)")
a = input("> ")

if a == "Yes":
    print("Wspaniale. Ruszajmy więc po przygodę!")
    print("""
    \rRok 1023 II ery
    \rGodzina 12.00
    \rPrzechadzasz się ulicą tętniącego życiem miasteczka. Nagle ktoś mija cię z biegnąc w przeciwną stronę.
    \rDecydujesz się za nim podążyć?(Yes/No)
    """)
    b = input("> ")

    if b == "Yes":
        print("""
        \rPodążasz za człowiekiem bięgnącym coraz wolniej, jakby uważał że zmylił pościg. 
        \rSkręca w mniej ruchliwą uliczkę na przedmieściach.
        \rW końcu zatrzymuje się w jakimś zaułku. Wyglada że cię nie zauważył.
        \rStoi do ciebie tyłem i przesuwa palcami po ścianie budynku jakby czegoś szukał.
        \rZastanawiasz się czy podejście do niego będzie dobtym pomysłem.
        \rMoże lepiej pozostać w ukryciu.
        \rChcesz podejść do nieznajomego?(Yes/No)
        """)
        c = input("> ")
            #ścieżka do zrobienia
        print("""
        \rTa ścieżka nie jest jeszcze gotowa... dzięki za przetestowanie dema ;)
        """)

    elif b == "No":
        print("""
        \rWzruszasz ramionami i idziesz dalej ulicą jakby nic się nie stało. 
        \rPo chwili zatrzymuje cię paru strażników, którzy wyglądają jakby kogoś szukali.
        \rChcesz im opowiedzieć o człowieku który cię minął?(Yes/No)
        """)
        c = input("> ")

        if c == "Yes":
            print("""
            \rWskazujesz strażnikom drogę, a oni ruszają w pościg za nieznajomym.
            \rWidzisz kątem oka że na dachu coś się poruszyło.
            \rWzruszasz ramionami ruszając w stronę domu.
            \rOtwierasz drzwi i przechodzisz przed próg.
            \rNagle czujesz jak coś wbija się w twoje ciało.
            \rSiły opuszczają twoje ciało a z szyji cieknie krew.
            \rPrzed tobą stoi człowiek podobny do tego który cię mijał.
            \rTrzyma w ręce małą kuszę z której do ciebie strzelił.
            \r- Zły wybór - mówi. - Oczy widzą, uszy słyszą, usta milczą.
            \rNieznajomy wychodzi podczas gdy umierasz na podłodze swojego pokoju.
            """)
            print("Koniec gry")

        elif c == "No":
            print("""
            \rTa ścieżka nie jest jeszcze gotowa... dzięki za przetestowanie dema ;)
            """)
            #wątek drugi

        else:
            print("\rWybrano odpowiedź z poza zakresu.")
            print("Koniec gry")


    else:
        print("\rWybrano odpowiedź z poza zakresu.")
        print("Koniec gry")

elif a == "No":
    print("Żegnaj")

else:
    print("\rWybrano odpowiedź z poza zakresu.")
    print("Koniec gry")