#creazione di un insieme (collezioni)
#non hanno un indice nella stampa sono delimitati da {}
a = set([1, 2, 3])
b = set([5, 6])
print(a)
print(b)
print(a | b) #unione di insiemi
print(a & b) #intersezioni di insiemi
b.remove(6)
print(b)