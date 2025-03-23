#psw: lettere minuscole alfabeto fatta da n caratteri come variabile globale
#alfabeto (21)
#ogni thread avrà come parametro la lettera

from threading import Thread
import time

global password
password = "zzzz"
trovata = False

class MioThread(Thread):
    def __init__(self, lettera, lista_lettere):
        super().__init__() #invocato il costruttore della classe precedente
        self.lettera = lettera
        self.lista_lettere = lista_lettere

    def run(self):
        cont = 0
        global trovata
        for c1 in self.lista_lettere:
            for c2 in self.lista_lettere:
                for c3 in self.lista_lettere:
                    cont += 1
                    pw = self.lettera + c1 + c2 + c3
                    if cont % 100 == 0:
                        print(f"Numero di password: {cont}")
                    if pw == password:
                        print("Password: " + pw)
                        trovata = True
                        break
                    if trovata:
                        return

def main():
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'z']
    lista_thread = [MioThread(l, alfabeto) for l in alfabeto]
    for t in lista_thread:
        t.start()

    for t in lista_thread:
        t.join()

if __name__ == "__main__":
    main()