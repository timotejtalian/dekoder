veta = input("Zadajte vetu: ").upper()
sifra = []

for pismeno in veta:
    if pismeno == " ":
        sifra.append("0")    
    else:
        znak = ord(pismeno) - 65
        vystup = znak // 3 + 1
        pocet = znak % 3 + 1
        sifra.append(str(vystup)*pocet)
print(" ".join(sifra))
print(veta)

string = "".join(sifra)
max_zoz = {}
for i in string:
    max_zoz[i] = string.count(i)
print(max_zoz)

max_hodnota = max(max_zoz.values())
najvacsie_kluce = [k for k, v in max_zoz.items() if v == max_hodnota]
print(" ".join(najvacsie_kluce))