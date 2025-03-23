dizionario = {"a":"albero", "b":"brutto", "c":"casa"} #una chiave un elemento
lista = ["albero", "brutto", "casa"]

print(dizionario["b"])
print(lista[1])
dizionario["d"] = "dado"
print(dizionario)
dizionario["a"] = "alto"
print(dizionario)

for chiave in dizionario:
    print(chiave)
    print(f"la chiave {chiave} ha valore {dizionario[chiave]}")

if "a" in dizionario: #ricerca
    print("a è presente")