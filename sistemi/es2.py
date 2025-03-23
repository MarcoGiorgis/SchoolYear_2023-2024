a = float (input("inserire un numero: "))
print(f"il tipo di a è {type(a)}")
if a > 5:
    print("a è maggiore di 5")
elif (a<=5) and (a>=0):
    print("a è maggiore o uguale a 0 o minore o uguale di 5")
else:
    print("a è minore di 0")