import turtle
def main():
    lista = []
    
    
    num = 5
    finestra = turtle.Screen()
    alice = turtle.Turtle()
    alice.speed(3)
    alice.begin_fill()
    for i in range(0, num):
        alice.forward(lista.f)
        alice.right(lista.r)
        alice.left(lista.l)
        #alice.penUp(100)
        #alice.forward(lung)
    alice.end_fill()

    finestra.mainloop()


if __name__ == "__main__":
    main()