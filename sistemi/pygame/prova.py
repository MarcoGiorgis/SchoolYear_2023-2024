from termios import CQUIT
import pygame
import sys
import random
#from pygame.locals import *

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

def calc_pav_random(n_rows, n_cols, probability_wall):
    """
    Genera un labirinto casuale con le dimensioni specificate.

    Args:
    - n_rows (int): Il numero di righe del labirinto.
    - n_cols (int): Il numero di colonne del labirinto.
    - probability_wall (float): La probabilità di avere un muro in una cella (da 0 a 1).

    Returns:
    - list: Una lista di liste rappresentante il labirinto generato casualmente.
    """
    maze = []
    for _ in range(n_rows):
        row = []
        for _ in range(n_cols):
            if random.random() < probability_wall:
                row.append(1)  # Muro
            else:
                row.append(0)  # Spazio libero
        maze.append(row)
    return maze

def draw_maze(screen, maze):
    wall_image = pygame.image.load("muro1.png")
    free_image = pygame.image.load("strada1.png")
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            x = j * 50
            y = i * 50
            if cell == 1:
                screen.blit(wall_image, (x, y))
            else:
                screen.blit(free_image, (x, y))

def main():
    n_rows = 10
    n_cols = 10
    probability_wall = 0.3  # Probabilità di avere un muro in una cella (da 0 a 1)

    pavimento = calc_pav_random(n_rows, n_cols, probability_wall)
    matrice = [[-1 for _ in range(n_cols)] for _ in range(n_rows)] #assegnazione di -1 a tutta la matrice

    sorg = int(input("Inserire il nodo sorgente: "))
    dest = int(input("Inserire il nodo destinazione: "))

    label, predecessori = dijkstra(sorg, pavimento)

    lista = [dest]
    prec = predecessori[dest]
    lista.append(prec)
    while prec != sorg:
        prec = predecessori[prec]
        lista.append(prec)
    lista = lista[::-1]

    print("Percorso più breve:", lista)

    pygame.init()
    screen = pygame.display.set_mode((n_cols * 50, n_rows * 50))
    pygame.display.set_caption("Labirinto Casuale")

    draw_maze(screen, pavimento)
    pygame.display.flip()

    done = False
    while not done:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                done = True
    pygame.quit()

if __name__ == "__main__":
    main()
