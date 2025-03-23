def codificaBinario(num):
    lista = []
    div = num
    while div > 0:
        r = div % 2
        if(r == 0):
            lista.append(r)
        else:
            lista.append(r)
        div = int(div / 2)
    print(lista[::-1])
        
def main():
    lista = []
    for k in range (0,4):
        IPdecimale = int(input("inserire l'ip in forma decimale: "))
        lista.append(IPdecimale)
    for num in lista:
        codificaBinario(num)
if __name__ == "__main__":
    main()