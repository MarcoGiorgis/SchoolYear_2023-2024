
#ripassare gestione file

class Testo:
    def __init__(self, testo_chiaro, chiave, lettere2numeri, numeri2lettere):
        self.testo_chiaro = testo_chiaro.lower()
        self.chiave = chiave.lower()
        self.lettere2numeri = lettere2numeri
        self.numeri2lettere = numeri2lettere

    def codifica(self):
        testo_criptato = ""
        for lettera_testo, lettera_chiave in zip(self.testo_chiaro, self.chiave): 
            numero = (self.lettere2numeri[lettera_testo] + self.lettere2numeri[lettera_chiave]) % 21
            testo_criptato += self.numeri2lettere[numero]
        return testo_criptato

    def decofica(self, testo_criptato):
        testo_decodificato = ""
        for lettera_testo, lettera_chiave in zip(testo_criptato, self.chiave):
            parola = (self.lettere2numeri[lettera_testo] - self.lettere2numeri[lettera_chiave]) % 21
            testo_decodificato += self.numeri2lettere[parola]
        return testo_decodificato

def main():
    lettere = "abcdefghilmnopqrstuvz"
    N = len(lettere)
    lettere2numeri = {}
    numeri2lettere = {}
    for posizione, lettera in enumerate(lettere):
        lettere2numeri[lettera]= posizione
        numeri2lettere[posizione]= lettera
        
    testo_chiaro = "ciao come stai?"
    chiave = "itisdelpozzo fprfrncnc rnfrfrovmc rmfcpdndpcs?"
    testo_criptato = ""
    testo_decodificato = ""
    
    for lettera_testo, lettera_chiave in zip(testo_chiaro, chiave): #cicla in parallelo sulle due parole fermandosi alla più corta
        numero = (lettere2numeri[lettera_testo] + lettere2numeri[lettera_chiave]) % N
        testo_criptato += numeri2lettere[numero]
    print(f"il testo in chiaro '{testo_chiaro}' diventa: '{testo_criptato}'")

    for lettera_testo, lettera_chiave in zip(testo_criptato, chiave):
        parola = (lettere2numeri[lettera_testo] - lettere2numeri[lettera_chiave]) % N
        testo_decodificato += numeri2lettere[parola]
    print(f"il testo codificato '{testo_criptato}' decofica '{testo_decodificato}'")
    

    t = Testo(testo_chiaro, chiave, lettere2numeri, numeri2lettere)
    testo_criptato = t.codifica()
    print(testo_criptato)
    print(t.decofica(testo_criptato))

if __name__ == "__main__":
    main()
