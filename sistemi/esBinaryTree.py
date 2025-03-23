import math

class Node():
    def __init__(self, valore):
        self.valore = valore
        self.sinistro = None
        self.destro = None

    def inserisci(self, valore):
        if self.valore is not None:
            #capire se inserire valore in figlio sinistro o destro
            if self.valore > valore:
                if self.sinistro == None:
                    self.sinistro = Node(valore)
                else:
                    self.sinistro.inserisci(valore)

            elif self.valore < valore:
                if self.destro == None:
                    self.destro = Node(valore)
                else:
                    self.destro.inserisci(valore)

        else: self.valore = valore
    
    def print_tree(self):
        #stampa solo i valori
        print(self.valore)
        
        if self.sinistro != None:
            self.sinistro.print_tree()
            
        if self.destro != None:
            self.destro.print_tree()

    def cercaValore(self, valore):
        #restituisce true o false
        if self.valore is not None:
            if valore == self.valore:
                return True
            elif valore < self.valore:
                    if self.sinistro != None:
                        return self.sinistro.cercaValore(valore)

            elif valore > self.valore:
                if self.destro != None:
                    return self.destro.cercaValore(valore)

            else:
                return False   
        else: 
            return False
        
    def counterNode(self, contNodi):
        contNodi += 1
        if self.sinistro is not None:
            contNodi = self.sinistro.counterNode(contNodi)
        if self.destro is not None:
            contNodi = self.destro.counterNode(contNodi)
        
        return contNodi
    
    def findHeight(self, altRight, altLeft):
        if self.sinistro is not None:
            altLeft = self.sinistro.findHeight(altRight, altLeft + 1)
        if self.destro is not None:
            altRight = self.destro.findHeight(altRight + 1, altLeft)

        return max(altRight, altLeft)
        
    def isBilanciato(self):
        return self.findHeight(0, 0) == int(math.log2(self.counterNode(0)))

def alberoBilanciato(lista,n):
    centro = len(lista)//2
    #print(lista)
    n.inserisci(lista[centro])
    if centro != 0:
        listaSx = lista[0 : centro]
        listaDx = lista[centro+1 :]
        if len(listaSx) > 0:
            alberoBilanciato(listaSx, n)
        if len(listaDx) > 0:
            alberoBilanciato(listaDx, n)
    else:
        return None

def main():
    n = Node(4)
    n.inserisci(1)
    n.inserisci(2)
    n.inserisci(3)
    n.inserisci(5)
    n.inserisci(6)
    n.inserisci(7)
    n.print_tree()
    """
    if (n.cercaValore(7)):
        print("Trovato")
    else:
        print("Non trovato")

    if (n.cercaValore(3)):
        print("Trovato")
    else:
        print("Non trovato")

    n1 = Node(None)
    lista = [5, 6, 2, 20, 28, 16]
    lista.sort()
    alberoBilanciato(lista, n1)
    n1.print_tree()
    """

    print("Numero nodi: " + str(n.counterNode(0)))
    print("Altezza dell'albero: " + str(n.findHeight(0, 0)))
    if n.isBilanciato() == True:
        print("è bilanciato")
    else:
        print("non è bilanciato")

if __name__ == "__main__":
    main()

