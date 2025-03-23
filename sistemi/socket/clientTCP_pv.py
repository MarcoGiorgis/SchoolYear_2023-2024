import socket

SERVER_ADDRESS = ("127.0.0.1", 9000)
BUFFER_SIZE = 4096

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    while True:
        messagio = input("Inserire cliente: ")
        s.sendall(messagio.encode())
        message = s.recv(BUFFER_SIZE)
        print(f"<{message.decode()}>")
    
    s.close()

if __name__ == "__main__":
    main()