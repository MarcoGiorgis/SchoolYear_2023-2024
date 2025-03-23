import socket
import threading
import time

MY_ADDRESS = ("127.0.0.1", 9000)
BUFFER_SIZE = 4096

blocco = threading.Lock()

class Client_hadler(threading.Thread):
    def __init__(self, connection, file):
        super().__init__()
        self.connection = connection
        self.file = file
        self.running = True

    def run(self):
        while self.running:
            movimento = self.connection.recv(BUFFER_SIZE)
            if movimento.decode() != 0:
                with open(self.file, "r") as file:
                    saldoStr = file.readline()
                saldo = float(saldoStr)
                if saldo > 0:
                    cifra = float(movimento) * saldo / 100
                    time.sleep(1) 
                    saldo -= cifra
                    blocco.acquire()
                    with open(self.file, "w") as file:
                        file.write(str(saldo))
                    blocco.release() 
                    print(f"Il saldo aggiornato è: {saldo}")
                    messagio = f"Saldo: {saldo}"
                    time.sleep(1)
                else:
                    print("saldo in negativo")
                self.connection.sendall(messagio.encode())
            else:
                self.connection.sendall("Chiusura in corso".encode())
                self.running = False
                self.connection.close()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()

    while True:
        connection, client_address = s.accept()
        print(f"Il client {client_address} si è connesso")
        thread = Client_hadler(connection, "saldo.txt")
        thread.start()

if __name__ == "__main__":
    main()