def main():
    op = int(input("inserire l'operazione da fare [0 = somma, 1 = sottrazione, 2 = moltiplicazione, 3 = divisione]"))
    a = float(input("inserire il primo valore: "))
    b = float(input("inserire il secondo valore: "))
    if(op == 0):
        ris = a + b
    elif(op == 1):
        ris = a - b
    elif(op == 2):
        ris = a * b
    elif(op == 3):
        ris = a / b
    else:
        print("operatore inserito non valido")

    print(f"il risultato è: {ris}")


if __name__ == "__main__": #per eseguire il main
    main()