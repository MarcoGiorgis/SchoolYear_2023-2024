#client
import socket
from threading import Thread

SERVER_ADDRESS = ("192.168.1.112", 9000)
BUFFER_SIZE = 4096

class MioThread(Thread):
    def __init__(self, s):
        super().__init__()
        self.s = s

    def run(self):
        #codice del thread
        while True:
            data, sender_address = self.s.recvfrom(BUFFER_SIZE)
            print(f"Ricevuto {data.decode()} da {sender_address}")

def main():
    ready = True
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    t = MioThread(s)
    while True:
        string = input("-> ")
        s.sendto(string.encode(), SERVER_ADDRESS) #per trasmettere stringhe binarie
        if ready:
            t.start()
            ready = False

if __name__ == "__main__":
    main()