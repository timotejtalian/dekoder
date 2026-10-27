import random
f = open(r"vstupny_text.txt", encoding = "utf-8")
sifra = ""
metoda = str(input("S/D: ")).lower()

for riadok in f:
    if metoda == "s":
        r_posun = random.randint(1,26) 
        r_char = chr(r_posun + 96)
        sifra += r_char
    else:
        r_posun = (riadok[0] + 96) 
        continue
    for znak in range(len(riadok)):
        if "a" <= riadok[znak] <= "z":
            if metoda == "s":
                sifra += chr(((((ord(riadok[znak])) - 96) + r_posun) % 26) + 96)
            else:
                sifra += chr(((((ord(riadok[znak])) - 96) - r_posun) % 26) + 96)
        else:
            sifra += riadok[znak]
f2 = open("mak.txt", "w", encoding = "utf-8")
f2.write(sifra)
f2.close()
f.close()