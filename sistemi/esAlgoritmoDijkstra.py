
"""
def calcoloAlgoritmo(grafo, sorgente):
    pass

def main():
    grafo = { #chiave esterna -> i diversi nodi / chiave interna i collegamenti con gli altri nodi / elemento interno peso del ramo
    0: {2: 3, 3: 5},
    1: {2: 2, 4: 1},
    2: {0: 3, 1: 2, 3: 7},
    3: {0: 5, 2: 7, 4: 4},
    4: {1: 1, 3: 4}
    }

    peso_arco34 = grafo[3][4]
    print(peso_arco34)
    print(grafo)

if __name__ == "__main__":
    main()
"""
"""
se si importa la libreria sys è presente una costante sys.maxsize() -> valore numerico più grande che gestisce il sistema
"""
import heapq
import sys

def dijkstra(grafo, nodo_iniziale):
    # Inizializzazione delle strutture dati
    distanze = {nodo: float('infinity') for nodo in grafo}
    distanze[nodo_iniziale] = 0
    coda_prioritaria = [(0, nodo_iniziale)]

    while coda_prioritaria:
        distanza_attuale, nodo_attuale = heapq.heappop(coda_prioritaria)

        # Ignora se abbiamo già trovato un percorso più breve
        if distanza_attuale > distanze[nodo_attuale]:
            continue

        # Scorre i vicini del nodo attuale
        for vicino, info_arco in grafo[nodo_attuale].items():
            peso_arco = info_arco['peso']
            nuova_distanza = distanze[nodo_attuale] + peso_arco

            # Aggiorna la distanza se è più breve
            if nuova_distanza < distanze[vicino]:
                distanze[vicino] = nuova_distanza
                heapq.heappush(coda_prioritaria, (nuova_distanza, vicino))

    return distanze

# Usa la funzione dijkstra con il tuo grafo
grafo = {
    0: {2: {'peso': 3, 'label': 'A'}, 3: {'peso': 5, 'label': 'B'}},
    1: {2: {'peso': 2, 'label': 'C'}, 4: {'peso': 1, 'label': 'D'}},
    2: {0: {'peso': 3, 'label': 'E'}, 1: {'peso': 2, 'label': 'F'}, 3: {'peso': 7, 'label': 'G'}},
    3: {0: {'peso': 5, 'label': 'H'}, 2: {'peso': 7, 'label': 'I'}, 4: {'peso': 4, 'label': 'J'}},
    4: {1: {'peso': 1, 'label': 'K'}, 3: {'peso': 4, 'label': 'L'}}
}

nodo_iniziale = 0
distanze_minime = dijkstra(grafo, nodo_iniziale)

# Stampa le distanze minime dai nodi iniziali a tutti gli altri nodi
for nodo, distanza in distanze_minime.items():
    print(f"Distanza minima dal nodo {nodo_iniziale} al nodo {nodo}: {distanza}")
