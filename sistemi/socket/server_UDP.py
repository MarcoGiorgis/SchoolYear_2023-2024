import socket

MY_ADDRESS = ("127.0.0.1", 9000) #identifica il processo server (indirizzo loopback, porta)
BUFFER_SIZE = 4096 #byte

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #s istanza classe socket
s.bind(MY_ADDRESS) #lega l'indirizzo al socket
while True:
    data, sender_address = s.recvfrom(BUFFER_SIZE)
    string = data.decode() #per codificare stringa da binaria a stringa
    print(f"Ricevuto {string} da {sender_address}")
    s.sendto(data, sender_address)
    if string == "EXIT":
        break