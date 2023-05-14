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