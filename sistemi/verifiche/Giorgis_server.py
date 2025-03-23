import socket
import threading
import time

MY_ADDRESS = ("127.0.0.1", 9000)
BUFFER_SIZE = 4096

blocco = threading.Lock()

class Client_hadler(threading.Thread):
    def __init__(self, connection, rubrica):
        super().__init__()
        self.connection = connection
        self.rubrica = rubrica
        self.running = True

    def run(self):
        while self.running:
            message = self.connection.recv(BUFFER_SIZE)
            messageCompleto = str(message.decode()).split("|")
            print(messageCompleto)
            if messageCompleto[0] == "Cerca-numero":
                if messageCompleto[1] in self.rubrica:
                    self.connection.sendall(str(self.rubrica[messageCompleto[1]]).encode())
                    #self.running = False
                else:
                    self.connection.sendall("Nome non trovato".encode())
            elif messageCompleto[0] == "Cerca-nome":
                for i in self.rubrica:
                    print(self.rubrica[i])
                    if messageCompleto[1] == self.rubrica[i]:
                        self.connection.sendall(str(i).encode())
                        #self.running = False
                    else:
                        self.connection.sendall("Numero di telefono non trovato".encode())
            elif messageCompleto[0] == "Aggiungi-contatto":
                aggiuntaNumero = str(messageCompleto[1]).split(";")
                with blocco: #porzione del codice che deve esssere eseguita da un solo thread alla volta
                    self.rubrica[aggiuntaNumero[0]] = aggiuntaNumero[1]
                    self.connection.sendall("ok".encode()) 
            else:
                self.connection.sendall("Errore nell'invio del messaggio".encode())


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()

    rubrica_telefonica = {
        "Mario Rossi": "123-456-7890",
        "Luca Bianchi": "234-567-8901",
        "Giulia Verdi": "345-678-9012",
        "Elena Neri": "456-789-0123",
        "Roberto Russo": "567-890-1234"
    }

    while True:
        connection, client_address = s.accept()
        print(f"Il client {client_address} si è connesso")
        thread = Client_hadler(connection, rubrica_telefonica)
        thread.start()

if __name__ == "__main__":
    main()