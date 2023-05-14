menu = {
    "Pizza Margharita": 25,
    "Pizza Funghi": 29,
    "Pizza Rusticana": 30,
    "Pizza Wegetariańska": 31,
    "Pizza Capricciosa": 32,
    "Pizza Tonno": 33,
    "Pizza ze szpinakiem": 34,
    "Pizza tropikalna": 34,
    "Pizza Pollo": 35,
    "Pizza Napoli": 35
}

sorted(menu)
lista1 = list(menu.keys())[0]
lista2 = list(menu.keys())[-1]
del menu[lista2]
del menu[lista1]


for klucz, wartosc in menu.items():
    print()
    print(klucz)
    print(wartosc)
    print(klucz, wartosc)

test = input("Czy chcesz dodać produkt? (y/n)")
if(test=='y'):
    produkt = input("Podaj nazwę produktu: ")
    cena = int(input("Podaj cenę produktu"))
    menu['produkt'] = cena
    print("Dodano produkt {} z ceną {}".format(produkt,cena))


