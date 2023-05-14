n = int(input("Podaj długość ciągu: "))
kolejne_liczby = []

for x in range(n):
    if(x==0 or x==1):
        kolejne_liczby.append(1)
    else:
        kolejne_liczby.append(kolejne_liczby[-1]+kolejne_liczby[-2])
print(kolejne_liczby)
