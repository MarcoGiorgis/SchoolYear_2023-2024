def main():
    max = 10
    power = [[k * i for i in range (1, max + 1)] for k in range (1, max + 1)]

    for k, tabellina in enumerate(power): #fuzione che enumera le site ritorna l'indice e l'elemento
        #tabellina == lista
        #power = lista di liste
        print(f"Tabellina del {k+1}: {tabellina}")
    
    file = open("tabellina.txt", "w") #file 
    for k in range (max):
        file.write(f"Tabellina del {k+1}: {tabellina}\n")
    file.close

if __name__ == "__main__":
    main()