import threading
import time

lock = threading.Lock() #variabile globale
#fa accedere alla sezione critica il numero di thread equivalente al parametro (2 = 2 thread)
semaforo = threading.Semaphore(1) #equivale alla lock 1 thread alla volta

class StampaNome(threading.Thread):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome

    def run(self):
        for _ in range(5):
            with semaforo:
                print("Ciao ", end="")
                time.sleep(1)
                print(self.nome)

def main():
    nomi = ["Mario", "Luca", "Alice", "Bob"]
    listaThread = [StampaNome(nome) for nome in nomi]
    for t in listaThread:
        t.start()
    for t in listaThread:
        t.join()

if __name__ == "__main__":
    main()