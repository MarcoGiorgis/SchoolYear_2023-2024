import socket

SERVER_ADDRESS = ("127.0.0.1", 9000)
BUFFER_SIZE = 4096

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    while True:
        messagio = input("Inserire movimento: ")
        s.sendall(messagio.encode())
        message = s.recv(BUFFER_SIZE)
        print(f"Ricevuto <{message.decode()}> dal server")
        if messagio == 0:
            break
    s.close()

if __name__ == "__main__":
    main()