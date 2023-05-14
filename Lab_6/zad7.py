import random

wybrane_liczby = 0
wygrywajace= 0

trafione = 0
k=6
#Wybrane liczby można zamienić 6-cio krotnym inputem
wybrane_liczby= (random.sample(range(1,49), 6))
wygrywajace=(random.sample(range(1,49),6))
for i in range(len(wybrane_liczby)):
    for j in range(len(wygrywajace)):
        if wybrane_liczby[i]==wygrywajace[j]:
            trafione=+1
print(wygrywajace)
print(wybrane_liczby)
print("Trafiłeś {}".format(trafione))