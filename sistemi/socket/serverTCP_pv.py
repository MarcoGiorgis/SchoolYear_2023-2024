#gestione di una coda con client-server
#se client già presente non viene messo
#ogni persona rimane in coda per 30 secondi

import socket
import threading
import time

MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096
lista=[]

class ClientHandler(threading.Thread):
    def _init_(self, connection):
        super().__init__()
        self.connection=connection
        
    def run(self):
        global lista
        message = self.connection.recv(BUFFER_SIZE)
        name=message.decode()
        if name not in lista:
            print(f"aggiunto in lista {name}")
            lista.append(name) 
            self.connection.sendall(f"prenotazione numero {len(lista)}".encode())
        else:
            self.connection.sendall(f"prenotazione gia effettuata, è in coda".encode())
        self.connection.close()

class Timer(threading.Thread):
    def _init_(self):
        super()._init_()
    
    def run(self):
        global lista
        while True:
            if len(lista)!=0:
                time.sleep(30)
                lista=lista[1:]
                print(lista)
        
def main():
    threadTime=Timer() 
    threadTime.start()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()
    while True:
        connection, _ = s.accept()
        thread = ClientHandler(connection)
        thread.start()
    s.close()

if __name__ == "__main__":
    main()