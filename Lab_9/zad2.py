import random

A ={'Paris Saint-Germain','RC Lens','Olympique Marsylia','Stade Rennais','AS Monaco','FC Lorient','OSC Lille','Olympique Lyon','Clermont Foot','Stade de Reims'}
B ={'Legia Warszawa','Wisła Kraków','Górnik Zabrze','Ruch Chorzów','Lech Poznań','ŁKS Łódź','Widzew Łódź','Stal Mielec','Śląsk Wrocław','Cracovia'}
lista = []
C=A|B
listC = list(C)
for i in range(4):
    listy1 = set([])
    for j in range(10):
        listy1.add(listC[random.randint(0,19)])
    lista.append(listy1)
for i in range(len(lista)):
    print(str(lista[i])+" Długość {}".format( len(lista[i])))
print()
print("Części wspólne 1 i 2 zbioru: {}".format(lista[1].intersection(lista[2])))
print("Elementy z 1 zbioru które nie są w 2 zbiorze: {}".format(lista[1].difference(lista[2])))
print("Jeżeli wszystkie elementy ze zbioru 2 znajdują się w 1 zwróci True: {}".format(lista[1].issuperset(lista[2])))
print("Jeżeli wszystkie elementy ze zbioru 1 znajdują się w 2 zwróci True: {}".format(lista[1].issubset(lista[2])))
print("Unia:{}".format(lista[1]|lista[2]))
