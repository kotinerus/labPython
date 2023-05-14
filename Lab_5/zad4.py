def nalezyDoPrzedialu(z):
     if(z>=-6 and z<=6):
        return print("Należy do przedziału")
     else:
        return print("Nie należy do przedziału")

n = int(input("Podaj ilość liczb: "))
for i in range(0,n):
    liczba = int(input("Podaj liczbę: "))
    nalezyDoPrzedialu(liczba)
