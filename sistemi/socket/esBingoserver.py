import threading
import socket
import random 

MY_ADDRESS = ("127.0.0.1", 9000)
BUFFER_SIZE = 4096

blocco = threading.Lock()

class Client_hadler(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
        self.running = True
        
    def run(self):
        global vincitore
        vincitore = None
        while self.running:
            try:
                message = self.connection.recv(BUFFER_SIZE)
                number = int(message.decode())
            except:
                print("Errore nel messaggio")
            with blocco:
                if not vincitore:
                    if number == random_number:
                        print(f"Vittoria di {self.connection}")
                        self.connection.sendall("Hai vinto".encode())
                        vincitore = self.connection
                        self.running = False
                    else:
                        if number > random_number:
                            self.connection.sendall(f"Numero inserito troppo alto".encode())
                        else:
                            self.connection.sendall(f"Numero inserito troppo basso".encode())
                else:
                    self.connection.sendall("Hai perso".encode())
                    self.running = False
            #self.connection.close()
    
    def kill(self):
        self.running = False

def main():
    global random_number
    random_number = random.randint(1, 100)
    print(random_number)

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