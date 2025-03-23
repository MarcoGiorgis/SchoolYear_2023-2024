import socket
import threading

MY_ADDRESS = ("127.0.0.1", 9000)
BUFFER_SIZE = 4096

class Client_hadler(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection

    def run(self):
        while True:
            message = self.connection.recv(BUFFER_SIZE)
            print(message.decode())
            messagio = input("-> ")
            self.connection.sendall(messagio.encode())

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()

    while True:
        connection, client_address = s.accept()
        print(f"Il client {client_address} si è connesso")
        thread = Client_hadler(connection)
        thread.start()

    s.close()

if __name__ == "__main__":
    main()