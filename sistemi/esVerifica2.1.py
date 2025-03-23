import random

def spostamentoCasuale(lista):
    return random.choice(lista) #sorteggia a caso un elemento della lista

def tempoTotale(giorni):
    return 60*60*24*giorni

def sommaTotale(lista):
    somma = 0
    for i in lista:
        somma += i
    return somma 
    
def main():
    numeriCasuali = [-1,1]
    listaCasuale = [spostamentoCasuale(numeriCasuali) for _ in range(0, tempoTotale(5))]
    print(sommaTotale(listaCasuale))
    #in python è possibile passare parametri con valori di default senza passare parametri nella chiamata
    #è possibile specificarne uno o entrambi 
    #spostamentoCasuale()
    #spostamentoCasuele(1000, [-3,3]) da mettere in ordine
    #se si mette anche il nome del parametro lo riconosce
    #spostamento(lista = [-1,1])
    #def spostamento(sec = 432000, lista[1,-1])

if __name__ == "__main__":
    main()