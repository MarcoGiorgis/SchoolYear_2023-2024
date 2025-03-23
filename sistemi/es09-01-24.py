import turtle
import random
import time

def nord(alice):
    alice.setheading(90)
    return alice.forward(10)

def sud(alice):
    alice.setheading(270)
    return alice.forward(10)

def est(alice):
    alice.setheading(0)
    return alice.forward(10)

def ovest(alice):
    alice.setheading(180)
    return alice.forward(10)

def main():
    finestra = turtle.Screen()
    alice = turtle.Turtle()

    movN = 0
    movS = 0
    movE = 0
    movO = 0

    dizionario = {"S" : sud, "N" : nord, "E" : est, "O" : ovest}
    dizionarioFinale = {"S": movS, "N": movN, "E": movE, "O": movO}
    possibiliCaratteri = ['S', 'N', 'E', 'O']
    listaCordinate = []
    listaCordinateDoppie = []
    
    durataCiclo = 60
    alice.goto(0,0)
    for _ in range(durataCiclo):
        cordinate = alice.pos()
        direzione = random.choice(possibiliCaratteri)
        dizionario[direzione](alice)
        dizionarioFinale[direzione] += 1

        if cordinate in listaCordinate:
            if not cordinate in listaCordinateDoppie: 
                listaCordinateDoppie.append(cordinate)
        
        listaCordinate.append(cordinate)
        time.sleep(1)

    with open("esercitazione.txt", "a") as file:
        file.write(str(listaCordinate))

    print(str(listaCordinate))
    print("Cordinate doppie: ")
    print(str(listaCordinateDoppie))
    print(str(dizionarioFinale))
    finestra.mainloop()
    
if __name__ == "__main__":
    main()