#in python tutto è pubblico 
#non servono quindi set e get
#non esiste overloading in python ovvero la chiamata di più costruttori con diversi parametri
class Quadrato():
    def __init__(self, lato): #è il costruttore si chiama in questo modo in tutte le classi
        self.lato = lato

    def calcolaArea(self): #è obbligatorio dare sempre self ad ogni metodo per riferirsci agli attributi
        return self.lato**2
    
    def stampaLato(self):
        print(f"il lato è {self.lato}")

def main():
    q = Quadrato(4) #si chiama il nome della classe che fa subito riferimento al costruttore
    print(f"l'area del quadrato q è {q.calcolaArea()}") #nelle chiamate non è presente il self
    print(q.lato) #non è privato
    q.lato = 5
    print(f"l'area del quadrato q è {q.calcolaArea()}")

if __name__ == "__main__":
    main()