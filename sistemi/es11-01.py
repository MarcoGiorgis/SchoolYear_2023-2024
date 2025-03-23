'''
chiedere un numero n dispari (controllo)
fare un rombo
'''

def main():
    lung = int(input("inserire un numero: "))
    while(lung % 2 != 1):
        lung = int(input("inserire un numero: "))

    for k in range(1, lung + 1, 2):
        print(" " * int((lung-k)/2) + "*" * k)
    
    for k in range(lung-2, 0, -2):
        print(" " * int((lung-k)/2) + "*" * k)
    
if __name__ == "__main__":
    main()
