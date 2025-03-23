import threading
import time

saldo = 1000
#creo oggetto di tipo lock, che è un blocco
blocco = threading.Lock()

class Prelievo(threading.Thread):
    def _init_(self, percentuale):
        super()._init_()
        self.percentuale = percentuale

    def run(self):
        global saldo
        while True:
            cifra = self.percentuale * (saldo / 100)
            time.sleep(1)
            
            #fa si che il primo thread che acquisisce la lock, sia l'unico operante
            #lo rilascia quando ha concluso l'operazione, è BLOCCANTE
            #Mutex = mutuamente esclusivo
            blocco.acquire()        #acquisisce la lock
            saldo = saldo - cifra   #esegue la zona critica
            blocco.release()        #rilascia la lock

            print(f"Il saldo aggiornato è {saldo}")
            time.sleep(5)

def main():
    luca = Prelievo(5)
    mario = Prelievo(-6)

    #concorrono all'operazione su una stessa variabile
    #La sezione critica di un thread è la porzione di codice
    #in cui il thread opera in scrittura sulla risorsa condivisa

    #race condition
    mario.start()
    luca.start()

if __name__ == "__main__":
    main()
