def contaNucleotidi(stringa):
    a, c, g, t = 0, 0, 0, 0
    for char in stringa:
        if char == "C":
            c += 1
        elif char == "A":
            a += 1
        elif char == "G":
            g += 1
        elif char == "T":
            t += 1
    return a, c, g, t

def contaNucleotidi2(stringa):
    dizNucleotidi = {"A": 0, "C": 0, "G": 0, "T": 0}
    for char in stringa:
        dizNucleotidi[char] += 1
    return dizNucleotidi

def contaNucleotidi3(stringa, nucleotide):
    return len([x for x in stringa if x == nucleotide])

def cercaProteinaSpike(stringa):
    proteinaSpike = "ATGTTTGTTTTT"
    for i, _ in enumerate(stringa[:-12]): 
        if stringa[i:i+len(proteinaSpike)] == proteinaSpike:
            return i
    return -1
        
def main():
    file = open("covid-19_gen1.txt", "r")
    righeFile = file.readlines()
    file.close()
    genoma = ""
    for riga in righeFile:
        #riga.replace("\n", "")
        riga = riga[:-1]
        genoma += riga

    a, c, g, t =  contaNucleotidi(genoma)

    print(f"A: {a}, C: {c}, G: {g}, T: {t}")
    print(contaNucleotidi2(genoma))
    posProtSpike = cercaProteinaSpike(genoma)
    print(posProtSpike)

if __name__ == "__main__":
    main()