class Quadrato():
    def __init__(self, lato, punto):
        self.lato = lato
        self.punto = punto
    
    def calcolaArea(self): 
        return self.lato**2
    
    def calcolaPerimetro(self):
        return self.lato * 4
    
    def puntoEstInt(self, x, y):
        if(x > 0 and x < self.lato and y > 0 and y < self.lato):
            return False
        else:
            return True

def main():
    quadrato = Quadrato(6, 7)
    print(f"Area: {quadrato.calcolaArea()}")
    print(f"Perimetro: {quadrato.calcolaPerimetro()}")
    x = int(input("inserire cordinata x: "))
    y = int(input("inserire cordinata y: "))
    if(quadrato.puntoEstInt(x, y) == True):
        print("punto esterno")
    else:
        print("punto esterno")

if __name__ == "__main__":
    main()