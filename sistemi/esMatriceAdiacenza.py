import networkx as nx
import matplotlib.pyplot as plt

def disegnaMatrice(dizionario):
    print(" ", end=" ")
    for k in range(0, 5):
        print(k, end=" ")

    print("\n")
    for k in range(0, 5):
        print(k, end="|")
        for j in range(0, 5):
            if j in dizionario[k]:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print("\n")

def stampaMatrice(matrice, separatore = "|"):
    for riga in matrice:
        print(separatore.join([str(x) for x in riga])) #passaggio da numeri a stringa

def conversioneMatriceDizionario(matrice):
    dizionario = {}
    k = 0
    for riga in matrice:
        j = 0
        lista = []
        for c in riga:
            if c == 1:
                lista.append(j)  
            j+=1
        dizionario[k] = lista
        k+=1
    print(dizionario)

def conversioneMatriceDizionario2(matrice):
    return {i: [j for j,n in enumerate(matrice[i]) if n != 0] for i in range(len(matrice))}

def disegnaGrafo(dizionario):
    G = nx.Graph()

    for nodo, archi in dizionario.items():
        for arco in archi:
            G.add_edge(nodo, arco)

    pos = nx.spring_layout(G)  # Layout per la disposizione dei nodi
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=8)
    plt.show()

def main():
    d = {0: [2, 3], 1: [2, 4], 2: [0, 1, 3], 3: [0, 2, 4], 4: [1, 3]}
    n = len(d)
    matrice = [[0] * n for _ in range(n)]

    for k, v in d.items(): #cicla sia su chiave che su valore
        for h in v:
            matrice[k][h] = 1

    stampaMatrice(matrice)
    conversioneMatriceDizionario(matrice)
    print(conversioneMatriceDizionario2(matrice))
    disegnaGrafo(d)
    
if __name__ == "__main__":
    main()