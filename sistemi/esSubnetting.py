def completa8bit(strbin):
    b = strbin[2:]
    l = len(b)
    return "0" * (8-l) + b

def main():
    ip = input("inserire l'ip: ")
    groups = ip.split(".") #split opposto di join 
    groups = [int(group) for group in groups]
    print(groups)
    groups_bin = [bin(group) for group in groups]
    print(groups_bin)
    for k in range(0,4):
        print(completa8bit(groups_bin[k]))
    print ("ciao" .join(groups_bin))

if __name__ == "__main__":
    main()