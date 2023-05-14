import math

n = int(input("Wprowadź ostatnią liczbę: "))
liczby = [True] * (n+1)
for i in range(2,math.ceil(math.sqrt(n))):
    if liczby[i]:
        for j in range(i**i,n+1,i):
            liczby[j]=False
for i in range(2,n+1):
    if liczby[i]:
        print(i)
