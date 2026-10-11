import random
kluc = input("Kluc: ").lower()
s_d = input("Sifra/Desifra: ").lower()

if s_d == "sifra":
    vstup = open("vstupny_text.txt", "r", encoding="utf-8").read()
    zasifrovat = True
else:
    vstup = open("vystup.txt", "r", encoding="utf-8").read()
    zasifrovat = False

def spracuj_text(vstup, kluc, zasifrovat):
    riadky = vstup.split("\n")
    vysledok = ""
    x = 0
    for i in range(len(riadky)):
        riadok = riadky[i]
        random_posun = 0
        if zasifrovat:
            random_posun = random.randint(1, 26)
            vysledok += chr(random_posun + 96)
        elif "a" <= riadok[0] <= "z":
            random_posun = ord(riadok[0]) - 96
            riadok = riadok[1:]
        for znak in riadok:
            if "a" <= znak <= "z":
                kl = ord(kluc[x % len(kluc)]) - 96
                ch = ord(znak) - 96
                if zasifrovat:
                    posun = (ch + kl + random_posun - 1) % 26 + 1
                else:
                    posun = (ch - kl - random_posun - 1) % 26 + 1
                vysledok += chr(posun + 96)
            else:
                vysledok += znak
            x += 1
        if i < len(riadky) - 1:
            vysledok += "\n"
            x += 1

    vystup = open("vystup.txt", "w", encoding="utf-8")
    vystup.write(vysledok)
    vystup.close()

spracuj_text(vstup, kluc, zasifrovat)
