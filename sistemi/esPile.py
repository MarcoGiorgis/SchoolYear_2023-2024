def push(pila, elemento):
    pila.append(elemento)

def pop(pila):
    x = pila.pop()
    return x

def main():
    pila = [1,2,3,4]
    push(pila, 10)
    print(pila)
    print(pop(pila), pila)

if __name__ == "__main__":
    main()