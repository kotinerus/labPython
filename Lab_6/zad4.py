lista_dzielnikow = []
liczba = int(input("Podaj liczbę: "))
for x in range(1,liczba):
    if liczba%x==0:
        lista_dzielnikow.append(x)
print(lista_dzielnikow)