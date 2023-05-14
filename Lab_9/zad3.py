class Kot():
    def __init__(self,wiek,rasa,kolor,plec,rodzenstwo):
        self.wiek = wiek
        self.rasa = rasa
        self.kolor = kolor
        self.plec = plec
        self.rodzenstwo = rodzenstwo

    def spanie(self):
        return "Kot śpi"
    def jedzenie(self):
        return "Kot je"
    def miauczenie(self):
        return "Kot miauczy"

    def __str__(self):
        return str(self.wiek)+' '+self.rasa+' '+self.kolor+' '+self.plec+' '+str(self.rodzenstwo)

kot1 = Kot(3,'perski','szary','m',4)
print(kot1)
