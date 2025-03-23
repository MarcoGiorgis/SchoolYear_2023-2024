'''un  robot può spostarsi su un pavimento con ostacoli; bisogna definire una mappa (in un file csv)
'''

"""
dizionario per movimenti:
0 : 0
1 : sys.maxsize()
2 ...

lista con i nodi non visitati
[1,2,...] si toglie i nodi che si visitano
"""
import pygame
import sys
from pygame.locals import *

class Grafo:
    def __init__(self):
        pass

def sceltaNodo(nonVisitati, label):
    minLabel = sys.maxsize
    minNodo = None
    for nodo in nonVisitati:
        labelNodo = label[nodo]
        if labelNodo < minLabel:
            minLabel = labelNodo
            minNodo = nodo
    return minNodo

def dijkstra(node_sorgente, matrice):
    n_nodi = len(matrice)
    nonVisitati = set([i for i in range(0, n_nodi)])
    label = {i : sys.maxsize for i in range(0, n_nodi)}
    predecessore = {}
    label[node_sorgente] = 0
    while(len(nonVisitati) > 0):
        nodo_corrente = sceltaNodo(nonVisitati, label)
        nonVisitati.remove(nodo_corrente)
        for nodoVicino, peso in enumerate(matrice[nodo_corrente]):
            if peso > 0:
                nuovaLabel = label[nodo_corrente] + peso
                if nuovaLabel < label[nodoVicino]:
                    predecessore[nodoVicino] = nodo_corrente
                    label[nodoVicino] = nuovaLabel
    return label, predecessore
    
def calc_pav(): #calcolate the array of array
    mat = [] 
    with open("percorso.csv", "r") as f:
        for riga in f.readlines():
            riga = riga.split(",")
            mat.append([int(c) for c in riga])
    return mat

def findFreeCell(pavimento, matrice): #find free cell
    cont = 0
    for indice_riga, riga in enumerate(pavimento):
        for indice_colonne, casella in enumerate(riga):
            if casella == 0:
                cont += 1
                matrice[indice_riga][indice_colonne] = cont
    return matrice

def findLenghtPoint(pavimento):
    dizDijstra = {}
    cont = 1
    primo = False
    for indice_riga, riga in enumerate(pavimento):
        for indice_colonne, casella in enumerate(riga):
            if casella == 0:
                if primo == False:
                    dizDijstra[1] = 0
                    primo = True
                else:
                    cont += 1
                    dizDijstra[cont] = sys.maxsize
    return dizDijstra
    

def main():
    """
    lato_x = 100
    lato_y = 100

    
    pavimento = calc_pav()
    n_y = len(pavimento)
    n_x = len(pavimento[0])
    matrice = [[-1 for _ in range(n_x)] for _ in range(n_y)] #assegnazione di -1 a tutta la matrice
    k = 1

    pygame.init()
    screen = pygame.display.set_mode((n_x * lato_x , n_y * lato_y))
    muro = pygame.image.load("muro1.png")
    strada = pygame.image.load("strada1.png")
    robot = pygame.image.load("robot.png")
    font = pygame.font.Font(None, 36) 
    
    #draw background
    for riga in pavimento:
        for casella in riga:
            surf1 = pygame.Surface((lato_x, lato_y))
            text = font.render(f"{k}", True, (0,0,0))
            if casella == 1:
                surf1.blit(muro, (0, 0))
                screen.blit(surf1, (lato_x-100, lato_y-100))  
            else:
                surf1.blit(strada, (0, 0))
                text_pos = text.get_rect(center=(lato_x-50, lato_y-50))  
                screen.blit(surf1, (lato_x-100, lato_y-100))  
                screen.blit(text, text_pos)
                k += 1
            
            pygame.display.flip()
            lato_x += 100
            
        lato_x = 100
        lato_y += 100
        screen.blit(robot, (10, 10))

    matrice = findFreeCell(pavimento, matrice)
    print(findFreeCell(pavimento, matrice))

    diz = {}
    for indice_riga, riga in enumerate(matrice):
        for indice_colonna, casella in enumerate(riga):
            if casella != -1:
                adiacenti = []
                if indice_colonna + 1 < len(riga) and matrice[indice_riga][indice_colonna + 1] != -1: #destra
                    adiacenti.append(matrice[indice_riga][indice_colonna + 1])
                if indice_colonna - 1 >= 0 and matrice[indice_riga][indice_colonna - 1] != -1: #sinistra
                    adiacenti.append(matrice[indice_riga][indice_colonna - 1])
                if indice_riga - 1 >= 0 and matrice[indice_riga - 1][indice_colonna] != -1: #sopra
                    adiacenti.append(matrice[indice_riga - 1][indice_colonna])
                if indice_riga + 1 < len(matrice) and matrice[indice_riga + 1][indice_colonna] != -1: #sotto
                    adiacenti.append(matrice[indice_riga + 1][indice_colonna])
                diz[casella] = adiacenti
    #trasformare il dizionario in matrice peso 1 passaggio, 0 nulla
    print(diz)
    print(findLenghtPoint(pavimento))
    
    matrice = [[0, 4, 0], [4, 0, 3], [0, 3, 0]]
    print(dijkstra(0, matrice))
    done = False
    while not done:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                done = True
    pygame.quit()
    """
    matrice = [[0, 4, 0], [4, 0, 3], [0, 3, 0]]
    sorg = int(input("inserire il nodo sorgente: "))
    dest = int(input("inserire il nodo destinazione: "))
    label, predecessori = dijkstra(sorg, matrice)
    print(label)
    print(predecessori)
    lista = [dest]
    prec = predecessori[dest]
    lista.append(prec)
    while prec != sorg:
        prec = predecessori[prec]
        lista.append(prec)
    lista = lista[::-1]
    print(lista)


if __name__ == "__main__":
    main()