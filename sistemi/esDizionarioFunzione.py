def somma(a, b):
    return a+b

def prodotto(a, b):
    return a*b

def sottrazione(a, b):
    return a-b

def divisione(a, b):
    return a/b

def main():
    dizionario = {"+" : somma, "*" : prodotto, "-" : sottrazione, "/" : divisione}
    operazione = input("scrivi un operazione (+ * - /): ")
    if operazione in dizionario: #controllo se operazione è una chiave
        a = float(input("inserire un numero: "))
        b = float(input("inserire un secondo numero: "))
    print(dizionario[operazione](a, b)) #operazione di tipo funzione -> richiamata nel dizionario
if __name__ == "__main__":
    main()