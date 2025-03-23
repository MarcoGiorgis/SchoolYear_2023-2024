import threading
import socket

MY_ADDRESS = ("127.0.0.1", 9000)
BUFFER_SIZE = 4096

class Client_hadler(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
        self.running = True

    def run(self):
        primo = False
        while True:
            message = self.connection.recv(BUFFER_SIZE)
            utente = message.decode().split(":")
            print(utente)
            if float(utente[1]) > 70:
                self.connection.sendall(f"Allarme temperatura, {utente[0]}".encode())
                primo = True
            if primo == True:
                if float(utente[1]) < 70:
                    self.connection.sendall(f"Allarme rientrato, {utente[0]}".encode())
                else:
                    self.connection.sendall(f"Allarme temperatura, {utente[0]}".encode())

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()
    while True:
        connection, client_address = s.accept()
        print(f"Il client {client_address} si è connesso")
        thread = Client_hadler(connection)
        thread.start()

if __name__ == "__main__":
    main()