abc = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
f = open("tabulka_pocetnosti.txt","r")
#print(f.read())

text = f.read().replace("\n","")
for pismeno in text:
    pismeno = pismeno.upper()
    if pismeno in abc:
        abc[pismeno] += 1

ab = abc.copy() 
znaky = []       
for i in abc:
    if abc[i] == 0:
        del ab[i]
        znaky.append(i)
print("Znaky", ", ".join(znaky), "sa v texte nevyskytli")

print("Pocetnost pismen v texte:")
for i in ab:
    print(i,"-",ab[i])

f.close()


