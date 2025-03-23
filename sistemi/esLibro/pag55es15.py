def main():
    nome = str(input("inserire un nome: "))
    print(nome[0] + "*" * (len(nome)-1))

if __name__ == "__main__":
    main()