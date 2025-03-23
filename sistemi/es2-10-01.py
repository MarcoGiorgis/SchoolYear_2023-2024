import turtle
import random
import time

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():
    finestra = turtle.Screen()
    alice = turtle.Turtle()
    lung = 10
    percorso = {0: Punto(0,0)}
    possibiliCaratteri = ['S', 'N', 'E', 'O']

    for tempo in range(1, 60):
        direzione = random.choice(possibiliCaratteri)
        if (direzione == "S"):
            percorso[tempo] = Punto(percorso[tempo-1].x, percorso[tempo-1].y + lung)
        if (direzione == "N"):
            percorso[tempo] = Punto(percorso[tempo-1].x, percorso[tempo-1].y - lung)
        if (direzione == "E"):
            percorso[tempo] = Punto(percorso[tempo-1].x + lung, percorso[tempo-1].y)
        if (direzione == "O"):
            percorso[tempo] = Punto(percorso[tempo-1].x - lung, percorso[tempo-1].y)
        
        alice.goto(percorso[tempo].x, percorso[tempo]. y)
        #controllo punto già percorso
        for k in range(tempo):
            if (percorso[k].x == percorso[tempo].x and percorso[k].y == percorso[tempo].y):
                print(f"Bob già passato in cordinate: {percorso[tempo].x}, {percorso[tempo].y}")
         

    with open("esercitazione2.txt", "w") as file:
        #ciclo su dizionario percorso
        file.write("Minuto" + "   " + "Posizione X" + "   " + "Posizione Y" + "\n")
        for minuto in percorso:
            posx = percorso[minuto].x
            posy = percorso[minuto].y
            file.write(str(minuto) + "   " + str(posx) + "    " + str(posy) +  "\n")
    finestra.mainloop()
    

if __name__ == "__main__":
    main()