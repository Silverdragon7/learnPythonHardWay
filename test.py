# # informacje o zmiennych dla kodu
# counter = 1
# plik = "1.txt"
# escape = 0
#
# #skrypt czytający
# def czyt(czytany):
#     return print(open(czytany).read())
#
# # skrypt pytający o odpowiedź i czytający odpowiedni plik
# def wybor(ans):
#     if ans == "Yes":
#         czyt(aktualnyt(counter))
#     elif ans == "No":
#         czyt(aktualnyn(counter))
#     else:
#         print("Wybrano odpowiedź z poza zakresu.")
#         exit()
#
# # wartości licznika i nazwy pliku
# def aktualnyt(counter):
#     counter = counter * 10
#     return f"{counter}.txt"
#
# # zmiana wartości licznika i nazwy pliku
# def aktualnyn(counter):
#     counter = counter * 10 + 1
#     return f"{counter}.txt"
#
#
# #funkcja szukająca frazy w pliku i podająca linię
# def szukaj(fraza, zrodlo):
#     counter = 1
#     with open(zrodlo, 'r') as read_obj:
#         for line in read_obj:
#             if f"{fraza}" in line:
#
#                 return counter
#             counter = counter + 1
#
# print(szukaj("lepiej", "0.txt"))

# def search_string_in_file(file_name, string_to_search):
#     line_number = 0
#     list_of_results = []
#     with open(file_name, 'r') as read_obj:
#         for line in read_obj:
#             line_number += 1
#             if string_to_search in line:
#                 list_of_results.append((line_number, line.rstrip()))
#     return list_of_results
#
# print(search_string_in_file("0.txt", "lepiej"))



# def zczytaj_wiecej_lini(linia, ilosci_lini, otwarty_plik):
#     msg = ' '
#     for zmienna in (1, ilosci_lini):
#         msg = msg + (otwarty_plik.readlines()[(linia + zmienna)])
#         zmienna =  zmienna + 1
#     return msg

# print(zczytaj_wiecej_lini(1, 5, open("1.txt")))


# print(open("1.txt").readlines()[3:6])

#
# def zczytaj_wiecej_lini(linia, ilosci_lini, otwarty_plik):
#     lista_linijek = ""
#     linia = linia - 1
#     ostatnia_linia = linia + ilosci_lini
#     lista_linijek = otwarty_plik.readlines()[linia:ostatnia_linia]
#     for zmienna in lista_linijek:
#         print(zmienna)
#
# print(zczytaj_wiecej_lini(2, 4, open("0.txt")))
#



#
# print(isinstance(zmienna, int))
#
# print(zmienna.is_integer())
#
# def is_int(zmienna):
#     if type(zmienna) == int:
#         return True
#     else:
#         if zmienna.is_integer():
#             return True
#         else:
#             return False
#
# print(is_int(zmienna))

lista = [5, 10, 24, 3]

lista.sort()
print(lista)











#
# def zczytaj_wiecej_lini(linia, ilosci_lini, otwarty_plik):
#     msg = ''
#     for zmienna in (1, ilosci_lini):
#         msg = msg + (otwarty_plik.readline(linia + zmienna))
#     return msg