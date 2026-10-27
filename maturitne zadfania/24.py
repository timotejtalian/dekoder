import random
f = open(r"mak.txt", encoding="utf-8")
metoda = str(input("S/D? ")).lower()
sifra = ""

for riadok in f:
    if metoda == "s":
        r_posun = random.randint(0, 25)
        sifra += chr(r_posun + 97)
    else:
        r_posun = ord(riadok[0]) - 97

    for znak in riadok:
        if "a" <= znak <= "z":
            if metoda == "s":
                sifra += chr((((ord(znak) - 97) + r_posun) % 26) + 97)
            else:
                sifra += chr((((ord(znak) - 97) - r_posun) % 26) + 97)
        else:
            sifra += znak

f2 = open("jano.txt", "w", encoding="utf-8")
f2.write(sifra)
f.close()
f2.close()