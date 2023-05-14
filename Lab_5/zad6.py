import random

liczba_wylosowana = random.randint(1,100)
for i in range(4):
    if (i == 3):
        print("Haha, przegrałeś")
        break
    liczba_uzytkownika = int(input("Stzrel {} liczbę".format(i+1)))
    if(liczba_uzytkownika==liczba_wylosowana):
        print("Wygrałeś w {} strzale".format(i+1))
        break
    elif liczba_uzytkownika>liczba_wylosowana:
        print("Podałeś za dużą wartość")
        continue
    else:
        print("Podałeś za małą wartość")
        continue
