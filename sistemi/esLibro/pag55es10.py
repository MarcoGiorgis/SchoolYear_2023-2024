lista_voti = []
k = 0
while True:
    voto = int(input("inserire un valore: "))
    if(voto < 0 and k >= 6):
        break
    lista_voti.append(voto)
    k = k + 1

print(lista_voti[1:-1])
lista_voti[3] = 10
print(lista_voti[:3])