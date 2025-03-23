import socket
import threading
import time

MY_ADDRESS = ("127.0.0.1", 9000)
BUFFER_SIZE = 4096

blocco = threading.Lock()
password = "abc"

class Client_hadler(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
        self.running = True

    def run(self):
        while self.running:
            pswUtente = self.connection.recv(BUFFER_SIZE)
            if pswUtente.decode() == password:
                self.connection.sendall("password trovata".encode())
                self.running = False
            else:
                self.connection.sendall("ritenta".encode())

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