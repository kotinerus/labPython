import random

lista = []
for x in range(10):
    lista.append(random.randint(1,100))
print(lista)
random.shuffle(lista)
print(lista)
lista.sort()
print(lista)