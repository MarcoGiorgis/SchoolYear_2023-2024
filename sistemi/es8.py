import turtle


def disegnaPoligoni(alice, lati, lung):
    angolo = 360/lati
    for i in range(0, lati):
        alice.forward(lung)
        alice.left(angolo)

def main():
    lung = int(input("inserire la lunghezza del lato:"))
    lati = 3

    finestra = turtle.Screen()
    alice = turtle.Turtle()
    alice.shape("turtle")
    alice.speed(3)
    alice.penup()
    alice.forward(-500)
    alice.pendown()

    for i in range (3, 12):
        alice.color("red")
        disegnaPoligoni(alice, lati, lung)
        alice.penup()
        alice.forward(100)
        alice.pendown()
        lati = lati + 1

    finestra.mainloop()

if __name__=="__main__":
    main()

