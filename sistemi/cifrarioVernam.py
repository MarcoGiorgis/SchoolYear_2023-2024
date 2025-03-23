'''
CIFRARIO DI VERNAM
a = 0
b = 1
c = 2 
.   .
fare in oltre una chiave per codificare la stringa
chiave a = 0 / b = 1 / c = 2 ...
fare la somma tra la stringa e la chiave e % 21

per codificare fare i passaggi inversi
tradurre la stringa - %21 - sottrarre la chiave
'''

class Testo:
    #deve poter visualizzare sia il testo codificato sia quello normale
    #parametri testo, chaive, codificato(boolean)
    def __init__(self, testo, chiave, codificato):
        self.testo = testo.lower()
        self.chiave = chiave.lower()
        self.codificato = codificato

    def cifra_cod(self, dizionario):
        if self.codificato == False:
            lista_chiave = [c for c in self.chiave] #crea una lista con i caratteri della stringa
            cifra = []
            for indice, char in enumerate(self.testo):
                cifra.append((dizionario[char] + dizionario[lista_chiave[indice]]) % 21)
            self.codificato = True
        else:
            print("la stringa è già codificata")

    #join attacca gli elementi di una lista con un carattere separatore

def main():
    str = input("Inserire una stringa: ")
    str = str.lower()
    dizionarioLettere = {}
    dizionarioNumeri = {}
    numeriLettere = 0
    for lettera in range(ord('a'), ord('z')+1):
        carattere = chr(lettera)
        if carattere in {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'z'}:
            dizionarioLettere[numeriLettere] = carattere
            numeriLettere += 1
    
    #cicla per chiave 
    #dizionario opposto
    for numero in dizionarioLettere:
        dizionarioNumeri[dizionarioLettere[numero]] = numero

    print(dizionarioLettere)
    print(dizionarioNumeri)

if __name__ == "__main__":
    main()