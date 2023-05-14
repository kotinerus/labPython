import random

listaA = []
listaB = []

for i in range(100):
    listaA.append(random.randrange(0,56)*2)
for j in range(100):
    listaB.append(random.randrange(0,56)*2+1)
tupA = tuple(listaA)
tupB = tuple(listaB)
print("Miejsce w pamięci tupA: {}".format(id(tupA)))
print("Miejsce w pamięci tupB: {}".format(id(tupB)))
tupleC = tupA+tupB
print("Miejsce w pamięci tupC: {}".format(id(tupleC)))
print("Długość: {}".format(len(tupleC)))
print("Wystąpienia 0: {}".format(tupleC.count(0)))
print("Wystąpienia 100: {}".format(tupleC.count(100)))
