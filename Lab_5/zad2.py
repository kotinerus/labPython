import random
import statistics

working = True
liczba_n = int(input("Podaj początek zakresu: "))
liczba_x = int(input("Podaj początek koniec: "))
if((liczba_x-liczba_n)<6):
    print("Zakres jest za mały")
    working=False

if working:
    liczby = []
    liczba_el = liczba_x-liczba_n
    for i in range(0,liczba_el):
        x = random.randint(liczba_n,liczba_x)
        if(x==0):
            print("Wpisano 0")
            break
        else:
            liczby.append(x)
    zakres = sorted(liczby[:6])
    print("Minimalna: "+str(min(zakres)))
    print("Maksimum: "+str(max(zakres)))
    print("Średnia: "+str(sum(zakres)/len(zakres)))
    print("Mediana: "+str(statistics.median(zakres)))