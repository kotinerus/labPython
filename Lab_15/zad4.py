bratAlbert = []
joachim = []

dostepneKarty = []
class Talia():
    def __init__(self ):
        self.iloscKart = 52
        self.kolor = ['Pik', 'Kier', 'Trefl', 'Karo']
        self.wartosc = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

    def dodawanieKartDoTali(self):
        for kolor in self.kolor:
            for wartosc in self.wartosc:
                dostepneKarty.append([kolor,wartosc])
element = Talia()
element.dodawanieKartDoTali()

counter = 0
for index,karta in enumerate(dostepneKarty):
   print(karta,end="")
   counter+=1
   if(counter==13):
       print('')
       counter=0

