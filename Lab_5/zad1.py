liczby = []
ile_liczb = int(input("Ile jest liczb? :"))

for i in range (0,ile_liczb):
    x = float(input("Podaj liczbę: "))
    if(x<0):
        continue
    else:
        liczby.append(x)
        print(sum(liczby)/len(liczby))
