slowo1 = input("Podaj słowo 1 ")
tuple1 = (slowo1)
litery1 = []
for i in range(len(slowo1)):
    litery1.append(slowo1[i])
litery1.sort()

slowo2 = input("Podaj słowo 2 ")
tuple2 = (slowo2)
litery2 = []
for i in range(len(slowo2)):
    litery2.append(slowo2[i])
litery2.sort()

if(litery1==litery2):
    print("Są anagramem")
else:
    print("Nie są anagramem")