import socket
import threading

SERVER_ADDRESS = ("127.0.0.1", 9000)
BUFFER_SIZE = 4096

trovato = False

class Find_pswThread(threading.Thread):
    def __init__(self, s, listaPsw):
        super().__init__()
        self.s = s
        self.listaPsw = listaPsw
        self.running = True

    def run(self):
        global trovato
        while self.running:
            if not trovato:
                for p in self.listaPsw:
                    self.s.sendall(p.encode())
                    message = self.s.recv(BUFFER_SIZE).decode()
                    print(f"Ricevuto <{message}> dal server")
                    if message == "password trovata":
                        trovato = True
                        self.running = False
                        break
            else:
                self.running = False

def main():
    global trovato
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    alfabeto = "abcdefghilmopqrstuvz"
    fileName = "password.txt"
    listaPsw = []

    with open(fileName, "w") as file:
        for primaLettera in alfabeto:
            for secondaLettera in alfabeto:
                for terzalettera in alfabeto:
                    file.write(f"{primaLettera}{secondaLettera}{terzalettera}\n")

    with open(fileName, "r") as file:
        p = file.readlines()
        for element in p:
            listaCorretta = element.split("\n")
            listaPsw.append(listaCorretta[0])

    half = len(listaPsw) // 2
    firstThread = Find_pswThread(s, listaPsw[:half])
    secondThread = Find_pswThread(s, listaPsw[half:])

    firstThread.start()
    secondThread.start()

    firstThread.join()
    secondThread.join()

    s.close()

if __name__ == "__main__":
    main()
