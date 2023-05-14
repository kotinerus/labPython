import random

liczba_n = int(input("Podaj ilość liczb: "))
liczba_a = int(input("Podaj początek zakresu: "))
liczba_b = int(input("Podaj koniec zakresu: "))
liczby = []
if(liczba_b-liczba_a<liczba_n):
    print("Zakres jest zbyt mały")
else:
    for i in range(liczba_n):
        liczby.append(random.randint(liczba_a,liczba_b))
        liczby = list(dict.fromkeys(liczby))
print("Długość: "+ len(liczby))
print(liczby)