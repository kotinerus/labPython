import random

liczby = []
ile_liczb = int(input("Ile jest liczb? :"))
zakres_kon = int(input("Jaka ma być ostania liczba zakresu? :"))
for j in range(0,ile_liczb):
    liczby.append(random.uniform(0,zakres_kon))

print(sum(liczby)/len(liczby))