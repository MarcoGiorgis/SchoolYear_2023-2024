#server
import socket
from threading import Thread
import time 

MY_ADDRESS = ("127.0.0.1", 9000) 
BUFFER_SIZE = 4096 

class MioThread(Thread):
    def __init__(self, s):
        super().__init__()
        self.s = s
        self.sender_address = None

    def run(self):
        #codice del thread
        while True:
            data, self.sender_address = self.s.recvfrom(BUFFER_SIZE)
            print(f"Ricevuto: {data.decode()} da {self.sender_address}")

    def getServerAddress(self):
        return self.sender_address

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    s.bind(MY_ADDRESS)
    t = MioThread(s)
    t.start()
    while True:
        if t.getServerAddress() != None:
            string = input("-> ")
            s.sendto(string.encode(), t.getServerAddress())

if __name__ == "__main__":
    main()
