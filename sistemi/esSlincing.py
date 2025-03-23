# SLICING di stringhe
s = "ciao come stai?" #indicizzazione a numeri negativi (ultimo carattere = -1)
print(f"il primo carattere è {s[0]}")
print(f"l'ultimo carattere è {s[-1]}")
print(f"il penultimo carattere è {s[-2]}")
print(f"l'ultimo carattere è {s[len(s)-1]}") # C-style

print(s[3:7]) #dal carattere 3 al carattere 7 escluso
print(s[1:-1]) #stampa tutta la stringa tranne il primo e ultimo carattere
print(s[1:]) #per stampare fino in fondo escluso il primo
print(s[:-1]) #per stampare tutta la stringa esculso l'ulitmo carattere
print(s) #per stampare tutta la stringa
print(s[::-1]) #stampa la stringa al contrario 
