#ista con i primi cinque quadrati perfetti
import random
quadrati = [i**2 for i in range(1,6)] #** simbolo di potenza 
numeri_interi = [i for i in range(1,11)] #lista con i primi 10 numeri

stringhe = ["computer", "cellulare", "laptop"]
stringhe_c = [parola for parola in stringhe if parola[0] == 'c']
voti = [random.randint(2,10) for _ in range(0, 10)] #voti random in una lista 
voti_insufficenti = [voto for voto in voti if(voto < 6)]
print(stringhe_c)
print(quadrati)
print(numeri_interi)
print(voti)
print(voti_insufficenti)