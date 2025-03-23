#lambda function: utile per definire funzioni brevi

def somma(a, b):
    return a + b

somma1 = lambda x, y: x+ y

x, y = 10, 4

lista = [10, 4]
print(somma(x, y))
print(somma1(x, y))
print(somma1(lista[0], lista[1]))

print(somma(*lista)) #spacchettamento della lista vincolo: lista con tanti elementi quanti i parametri della funzione