rubrica_telefonica = {
    'Mario': '123-456-7890',
    'Luca': '234-567-8901',
    'Anna': '345-678-9012',
    'Giulia': '456-789-0123'
}

def cerca_contatto(rubrica, chiave):
    """
    Cerca un contatto nella rubrica telefonica.
    :param rubrica: Dizionario con i contatti e i numeri di telefono.
    :param chiave: Nome o numero di telefono da cercare.
    """
    if chiave in rubrica:
        return rubrica[chiave]
    else:
        for nome, numero in rubrica.items():
            if numero == chiave:
                return nome
        return "Contatto non trovato"

def main():
    while True:
        print("\n1. Cerca per nome")
        print("2. Cerca per numero di telefono")
        print("3. Esci")

        scelta = input("Scegli un'opzione (1/2/3): ")

        if scelta == '1':
            nome_cercato = input("Inserisci il nome da cercare: ")
            risultato = cerca_contatto(rubrica_telefonica, nome_cercato)
            print(f"Risultato: {risultato}")

        elif scelta == '2':
            numero_cercato = input("Inserisci il numero di telefono da cercare: ")
            risultato = cerca_contatto(rubrica_telefonica, numero_cercato)
            print(f"Risultato: {risultato}")

        elif scelta == '3':
            print("Arrivederci!")
            break

        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()