def main():
    barra = int(input("inserire la dimensione della barra"))
    str = "1" * barra + "0" * (32 - barra)
    gruppo1 = int(str[0:8], 2)
    gruppo2 = int(str[8:16], 2)
    gruppo3 = int(str[16:24], 2)
    gruppo4 = int(str[24:], 2)
    
    ip = f"{gruppo1}.{gruppo2}.{gruppo3}.{gruppo4}"
    print(ip)
    #lista = [gruppo1, gruppo2, gruppo3, gruppo4]
    #lista = [str(elemento) for elemento in lista]
    #print("." .join(lista))


if __name__ == "__main__":
    main()