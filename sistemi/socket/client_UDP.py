import socket

SERVER_ADDRESS = ("127.0.0.1", 9000)
BUFFER_SIZE = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    string = input("-> ")
    s.sendto(string.encode(), SERVER_ADDRESS) #per trasmettere stringhe binarie
    data, sender_address = s.recvfrom(BUFFER_SIZE)
    print(f"Ricevuto {data.decode()} da {sender_address}")
    if string == "EXIT":
        break