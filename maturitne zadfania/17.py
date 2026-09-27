veta = input("Napiste vetu: ")
sifra = []
for pismeno in veta:
    if pismeno == " ":
        sifra.append("0")
    else:
        asci = ord(pismeno) - 65
        pocet = asci % 3 + 1
        cislo = asci // 3 + 1
        sifra.append(str(cislo) * pocet)
print(" ".join(sifra))


znaky = "".join(sifra)
pocty = []
for hodnota in znaky:
    pocet_hodnoty = znaky.count(hodnota)
    pocty.append(pocet_hodnoty)

max_h = max(pocty)
najcastejsie = []
for hodnota in znaky:
    pocet_hodnoty = znaky.count(hodnota)
    if pocet_hodnoty == max_h:
        if hodnota not in najcastejsie:
            najcastejsie.append(hodnota)

print("Najcastejsie policko:", " ".join(najcastejsie))