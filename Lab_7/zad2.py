import random
list = []
for x in range(100):
    list.append(random.randint(0,10))
list = tuple(list)
print(list)
wystapienia0 = 0
wystapienia1 = 0
wystapienia2 = 0
parzyste = 0
nieparzyste = 0
for i in range(len(list)):
    if list[i]==0:
        wystapienia0+=1
    elif list[i]==1:
        wystapienia1+=1
    elif list[i]==2:
        wystapienia2+=1
    if list[i]%2==0:
        parzyste+=1
    else:
        nieparzyste+=1
print("Wystąpienie 0: {}\nWystąpienie 1: {}\nWystąpienie 2: {}".format(wystapienia0, wystapienia1, wystapienia2))
print("Parzyste {}".format(parzyste))
print("Nieparzyste {}".format(nieparzyste))
