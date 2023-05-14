tupleA = ['ma', 'koń', 'dwa', 'pies', 'ania', 'jeleń']
zdanie = []
listaPow = []
zdanietext = input("Podaj zdanie:")
zdanie = zdanietext.lower().split()
for i in range(len(tupleA)):
    ilerazy = 0
    for j in range(len(zdanie)):
        if(zdanie[j]==tupleA[i]):
            print("Słowo {} zostało znalezione. Index to {}".format(zdanie[j],(tupleA).index(tupleA[i])))
            ilerazy += 1
    listaPow.append(ilerazy)
print()
for i in range(len(listaPow)):
    if(listaPow[i]!=0):
        print("Słowo {} znajduje się w zdaniu {} razy".format(tupleA[i], listaPow[i]))

