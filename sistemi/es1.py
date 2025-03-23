def main(): #definizione funzione main
    nome = input("come ti chiami?")
    anni = int(input("quanti anni hai?")) #input ritorna solo strighe
    anno_corrente = int(input("in quale hanno siamo? "))
    print(f"il tuo nome è {nome} e hai {anni} anni") #si mette f con stringa variabile
    print(f"se nato nel {anno_corrente-anni}")
    print("ciao") #la print va a capo da sola
    print(type(anni))

if __name__ == "__main__": #per eseguire il main
    main()