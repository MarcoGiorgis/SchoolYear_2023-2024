def main():
    a = int(input("inserire un numero: "))
    if(a % 2 == 0):
        print("numero divisibile per 2")
    elif (a % 3 == 0):
        print("numero divisibile per 3")
    elif (a % 5 == 0):
        print("numero divisibile per 5")
    else:
        print("numero non divisibile")

if __name__ == "__main__": #per eseguire il main
    main()