import random
import string

string.ascii_letters
tablica = []
for x in range(10):
    tablica.append(random.choice(string.ascii_letters))
print(tablica[1], tablica[4], tablica[7], tablica[9])