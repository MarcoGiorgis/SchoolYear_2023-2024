#liste
def print_list(l):
    print("La lista é: ", end=" ")
    for elemento in l:
        print(elemento, end=" ")
    print("\n")

def main():
    l = [1, 2, 3 ,4, "c", 3.14, "python"]
    r = [10, 11, 12]
    print_list(l+r) #concatena due liste
    print_list(3*r) #concatena la lista per tre volte utile anche con le stringhe
    print(l)
    #print(l[-1])

    print_list(l[::-1]) #inverte la lista

    #vogliamo permettere all'utente di caricare una lista
    lista = []
    num = 1
    while num > 0:
        num = int(input("Scrivi un numero: (-1 per interrompere): "))
        if num > 0:
            lista.append(num)
    print_list(lista)

if __name__=="__main__":
    main()