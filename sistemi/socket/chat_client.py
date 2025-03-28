#client
import socket
from threading import Thread

SERVER_ADDRESS = ("192.168.1.129", 8000)
MY_ADDRESS = ("192.168.1.112", 8000)
BUFFER_SIZE = 4096
NICKNAME = "Giorgis"

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
    s.bind(MY_ADDRESS)
    t = MioThread(s)
    while True:
        message = input("-> ")
        dest = input("inserire il nickname del destinatario: ")
        packet = f"{message}|{NICKNAME}|{dest}"
        s.sendto(packet.encode(), SERVER_ADDRESS) #per trasmettere stringhe binarie
        if ready:
            t.start()
            ready = False

if __name__ == "__main__":
    main()