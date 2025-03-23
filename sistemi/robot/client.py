import socket

SERVER_ADDRESS = ("192.168.1.146", 8000)  
BUFFER_SIZE = 4096  

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(SERVER_ADDRESS)
    
    print("Connected to the server. Type 'help' for a list of commands, 'exit' to quit.")
    
    try:
        while True:
            command = input("Enter command: ")
            
            if command == "exit":
                client.sendall(command.encode())
                response = client.recv(BUFFER_SIZE)
                print(response.decode())
                break
            
            client.sendall(command.encode())
            response = client.recv(BUFFER_SIZE)
            print(response.decode())
            
    except Exception as e:
        print(f"Error {e}")

    client.close()

if __name__ == "__main__":
    main()
