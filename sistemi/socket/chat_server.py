#server
import socket

MY_ADDRESS = ("0.0.0.0", 9000) #0.0.0.0
BUFFER_SIZE = 4096 

def caricaRubrica():
    rubrica = {}
    with open("rubrica.csv", "r") as file:
        next(file) #salta la prima riga
        for line in file:
            nickName, ip, porta = line.strip().split(",")
            rubrica[nickName] = (ip, int(porta))
    return rubrica

def main():
    rubrica = caricaRubrica()
    print(rubrica)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    s.bind(MY_ADDRESS)
    while True:
        data, sender_address = s.recvfrom(BUFFER_SIZE)
        print("Messaggio ricevuto da:", sender_address)
        elementMessage = data.decode().split("|")

        if len(elementMessage) == 3:
            message, nicnickName_mittente, nickName_destinatario = elementMessage
            if nickName_destinatario in rubrica:
                if message == "info_rubrica":
                    s.sendto(str(rubrica).encode(), (rubrica[nickName_destinatario]))
                try:
                    s.sendto(message.encode(), (rubrica[nickName_destinatario]))
                    print(f"mando a {nickName_destinatario} da {nicnickName_mittente} message: {message}")
                except:
                    print(f"errore causato da {sender_address}")
            else:
                print("persona ricercata non presente in rubrica")
        else:
            print("errore indirizzo ip destinatario")
            print(data.decode())

if __name__ == "__main__":
    main()
