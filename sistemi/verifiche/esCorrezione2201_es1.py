class Testo():
    def __init__(self, stringa):
        self.stringa = stringa
        self.lista = self.stringa.split(" ")

    def numero_caratteri(self):
        return len(self.stringa)
    
    def lista_parole(self):
        return self.lista
    
    def lunghezze_parole(self):
        return [len(parola) for parola in self.lista]
    
    def ricerca(self, parola):
        return parola in self.lista #ritorna come booleano
    
    def salva_file(self, nomeFile):
        with open(nomeFile, "w") as file:
            file.write(self.stringa)

    def frequenze_parole(self):
        frequenze = {}
        for parola in self.lista:
            if parola in frequenze:
                frequenze[parola] += 1
            else: 
                frequenze[parola] = 1
        return frequenze
    
def main():
    str = "ciao come stai?"
    t = Testo(str)
    print(t.numero_caratteri())
    print(t.lista_parole())
    print(t.lunghezze_parole())
    print(t.ricerca("mario"))
    print(t.ricerca("ciao"))
    t.salva_file("file.txt") 
    print(t.frequenze_parole())

if __name__ == "__main__":
     main()