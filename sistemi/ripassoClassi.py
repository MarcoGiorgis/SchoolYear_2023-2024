import random

class Nemico():
    def __init__(self, pos_x, pos_y, n_vite):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.n_vite = n_vite
    def stampa(self):
        print(f"Nemico in posizione {self.pos_x}, \ {self.pos_y} con {self.n_vite} vite")


def main():
    N_NEMICI = 5
    WIDTH = 800
    HEIGHT = 400
    listaNemici = []
    random.seed(1234) #seleziona il seme del generatore dei numeri pseudo casuali
    for _ in range(N_NEMICI):
        posX = random.randint(0, WIDTH-1)
        posY = random.randint(0, HEIGHT-1)
        nemico = Nemico(posX, posY, 5)
        listaNemici.append(nemico)
    print(listaNemici)

    personaggio = {"posizione_x":100,"posizione_y":200}
    for nemico in listaNemici:
        nemico.stampa()

if __name__ == "__main__":
    main()