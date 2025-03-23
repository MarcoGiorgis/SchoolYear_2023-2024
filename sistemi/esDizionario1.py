def ricerca(dizionario):
    c = -1
    numeri = "0123456789"
    a = input("Inserisci il nome o il numero che vuoi cercare: ")
    if (a[0] in numeri):
        #print("numero")
        for x in dizionario:
            if(x == int(a)):
                print(dizionario[x])
                c = 0
    else:
        #print("lettera")
        for x in dizionario:
            if (dizionario[x] == a):
                print(x)
                c = 0
    if (c == -1):
        print("Nome o numero non trovato")

def main():
    rubrica = {}
    file = open("rubrica.txt", "r")
    righe = file.readlines()
    file.close()
    print(righe)
    for riga in righe:
        campi = riga.split(", ") #restituisce una lista
        numeroTelefonico = int(campi[1].replace("\n", "")) #sostituisce un carattere con un altro in tal caso nulla
        nome = campi[0]
        rubrica[numeroTelefonico] = nome #numero telefonico come chiave
    print(rubrica)
    file.close
    ricerca(rubrica)
if __name__ == "__main__":
    main()