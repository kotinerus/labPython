
liczba_n = int(input("Podaj ile liczb chcesz wypisać: "))
liczba_x = int(input("Podaj początek zakresu: "))
liczba_z = int(input("Podaj koniec zakresu: "))
liczby = []
if(liczba_z-liczba_x<liczba_n):
    print("Zakres jest zbyt mały")
else:
    for i in range(liczba_n):
        liczby.append(liczba_x+i)
    print(liczby)
    liczba_k = int(input("Podaj który element od końca chcesz usunąć: "))
    if(liczba_k>len(liczby)):
        print("Nie da się tego zrobić")
    else:
        liczby.pop(-liczba_k)
liczba_n = int(input("Podaj ile liczb chcesz wypisać: "))
liczba_x = int(input("Podaj początek zakresu: "))
liczba_z = int(input("Podaj koniec zakresu: "))

if(liczba_z-liczba_x<liczba_n):
    print("Zakres jest zbyt mały")
else:
    for i in range(liczba_n):
        liczby.append(liczba_x+i)
print("Długość listy: "+str(len(liczby)))
same_liczby = list(dict.fromkeys(liczby))
for x in range(len(same_liczby)):
    print("Ilość liczby {} w liście: ".format(same_liczby[x])+str(liczby.count(same_liczby[x])))
print(liczby)