import turtle

def completa8bit(strbin):
    b = strbin[2:]
    l = len(b)
    return "0" * (8 - l) + b

def conversioneAsci(stringa):
    ascii_values = []
    for carattere in stringa:
        valore = ord(carattere)
        if valore <= 255:
            ascii_values.append(valore)
    return ascii_values

def conversioneBinaria(valori):
    binary_values = []
    for valore in valori:
        binary_value = bin(valore)
        binary_values.append(completa8bit(binary_value))
    return binary_values

class Barcode:
    def __init__(self, stringa):
        self.stringa = stringa 

    def disegnaCodice(self):
        finestra = turtle.Screen()
        alice = turtle.Turtle()
        alice.speed(100)
        alice.hideturtle()
        alice.penup()

        for valore_bin in self.stringa:
            for bit in valore_bin:
                if bit == "1":
                    alice.fillcolor("black")
                else:
                    alice.fillcolor("white")
                alice.begin_fill()
                for _ in range(2):
                    alice.forward(4)
                    alice.right(90)
                    alice.forward(100)
                    alice.right(90)
                alice.end_fill()
                alice.forward(1)
        turtle.done()
            


def main():
    ascii_values = []
    binary_values = []
    while True:
        stringa = input("inserire una stringa alfamunerica di otto caratteri: ")
        if len(stringa) <= 8:
            break
    ascii_values = conversioneAsci(stringa)
    binary_values = conversioneBinaria(ascii_values)
    code = Barcode(binary_values)
    code.disegnaCodice()

if __name__ == "__main__":
    main()