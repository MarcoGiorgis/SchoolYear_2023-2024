import turtle
'''per commentare tutto'''
punte = int(input("inserire numero di punte (con un minimo di 5 punte): "))
lung = int(input("inserire la lunghezza dei lati: "))

finestra = turtle.Screen()
alice = turtle.Turtle()
alice.speed(100)
alice.begin_fill()
angoloEsterno = 360/punte
angoloInterno = 180 - angoloEsterno
for i in range(0, punte):
    alice.color("red")
    alice.forward(lung)
    alice.right(angoloInterno)
    alice.forward(lung)
    alice.left(180 - angoloInterno)

alice.end_fill()
finestra.mainloop()