working=True
suma_szescianow=0
for i in range(1,101):
    suma_szescianow+=i**3
print("Suma sześcianów: "+str(suma_szescianow))


liczba_max = 10 **6
aktualna_liczba = 0
aktulana_suma=0
liczby = []
while working:
    if(aktulana_suma>liczba_max):
        print("Potrzebne liczby: "+str(len(liczby)))
        break
    else:
        aktualna_liczba+=1
        liczby.append(aktualna_liczba)
        aktulana_suma+=aktualna_liczba
