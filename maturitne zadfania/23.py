vstup = input("Vstup: ").lower()
kluc = input("Kluc: ").lower()
s_d = input("Sifra/Desifra: ")
klucc = kluc * len(vstup)
klucc = klucc[:len(vstup)]

if s_d == "sifra":
    Zasifrovat = True
else:
    Zasifrovat = False

def sifrovanie(vstup, klucc):
    sifra = ""
    for x in range(len(vstup)):
        if vstup[x] == " ":
            sifra += " "
        else:
            kl = ord(klucc[x]) - 96
            ch = ord(vstup[x]) - 96
            if Zasifrovat:
                posun = ch + kl
                if posun > 26:
                    posun -= 26
                sifra += chr(posun + 96)
            else:
                posun = ch - kl
                if posun < 1:
                    posun += 26
                sifra += chr(posun + 96)
    return sifra
print(sifrovanie(vstup, klucc))