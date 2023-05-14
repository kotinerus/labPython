ile_liczb = int(input("Ile liczb zamierzasz wpisać?"))
liczby = []
for i in range(ile_liczb):
    liczby.append(input("Podaj {} liczbę: ".format(i+1)))
print("Makszymalna liczba: {}".format(max(liczby)))
print("Liczba {} pojawiła się {} razy.".format(max(liczby),liczby.count(max(liczby))))