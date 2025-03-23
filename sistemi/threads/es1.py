from threading import Thread
import time

class MioThread(Thread):
    def __init__(self, nome):
        super().__init__() #invocato il costruttore della classe precedente
        self.nome = nome
        self.running = True

    def run(self):
        #codice del thread
        while self.running:
            print(f"Sono il thread {self.nome}")
            time.sleep(1)

    def kill(self):
        self.running = False

def main():
    """
    thread1 = MioThread("Alice") #un istanza di thread
    thread2 = MioThread("Bob")
    thread1.start()
    thread2.start()
    """
    listaNomi = ["Alice", "Bob", "Trudy"]
    lista_thread = [MioThread(n) for n in listaNomi]
    for t in lista_thread:
        t.start()
    for _ in range(4):
        print("Sono il main threads")
        time.sleep(1)
    for t in lista_thread:
        t.kill()
        t.join() 

if __name__ == "__main__":
    main()