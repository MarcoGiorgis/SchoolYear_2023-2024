import turtle
import time

time.sleep()

def nord(alice):
    alice.setheading(90)
    return alice.forward(100)

def sud(alice):
    alice.setheading(270)
    return alice.forward(100)

def est(alice):
    alice.setheading(0)
    return alice.forward(100)

def ovest(alice):
    alice.setheading(180)
    return alice.forward(100)

def main():
    finestra = turtle.Screen()
    alice = turtle.Turtle()
    dizionario = {"S" : sud, "N" : nord, "E" : est, "O" : ovest}
    while(True):
        direzione = input("inserire la direzione (S: sud N: nord E: est O: ovest)")
        if direzione in dizionario:
            dizionario[direzione](alice)
        finestra.mainloop
if __name__ == "__main__":
    main()