f = open("vstupny_text.txt", "r", encoding = 'utf-8')
p_kluc = str(input("Zadaj kluc ")).lower()
sifra = ""
f2 = open("joyo.txt","w",encoding = "utf-8",)
metoda = str(input("S/D: ")).lower()

for riadok in f:
    if not riadok:
        continue
    kluc = p_kluc * len(riadok)
    kluc = kluc[:len(riadok)]
    for znak in range(len(riadok)):
        if "a" <= riadok[znak] <= "z":
            if metoda == "s":
                s = chr((((ord(riadok[znak]) - 96) + (ord(kluc[znak]) - 96)) % 26) + 96)
                sifra += s
            else:
                s = chr((((ord(riadok[znak]) - 96) - (ord(kluc[znak]) - 96)) % 26) + 96)
                sifra += s
        else:
            sifra += riadok[znak]
f2.write(sifra)
