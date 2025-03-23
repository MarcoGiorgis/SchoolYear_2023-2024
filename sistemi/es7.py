import turtle

num = int(input("inserisci il numero di lati: "))
lung = int(input("inserire la lunghezza dei lati: "))

finestra = turtle.Screen()
alice = turtle.Turtle()
alice.speed(3)
alice.begin_fill()
for i in range(0, num):
    alice.forward(lung)
    alice.left(360/num)
    alice.color('purple')
    #alice.penUp(100)
    #alice.forward(lung)
alice.end_fill()

finestra.mainloop()