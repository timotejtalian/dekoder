f = open("C:\\Users\\titop\\Desktop\\Skola\\dekoder\\maturitne zadfania\\autobus.txt", "r", encoding="utf-8")

pocet_zastavok = sum(1 for line in f) - 1
print("Pocet zastavok:", pocet_zastavok)
f.seek(0)

kapacita = f.readline()
f.seek(0)
next(f)

final = []
i = 0
pocet_ludi = 0
najviac = 0
zastavka = ""
for riadok in f:
    riadok = riadok.strip()
    cast = riadok.split()          
    stanica = " ".join(cast[2:])  
    final.append(stanica)         
    pocet_ludi += (int(cast[0]) - int(cast[1]))
    if pocet_ludi > int(kapacita):
        zastavka += final[i] + ", "
        i += 1
        if najviac < (pocet_ludi - int(kapacita)):
            najviac = (pocet_ludi - int(kapacita))
        else:
            pass
    else: 
        i += 1

vysledok = ", ".join(final)
print("Zastavky:",vysledok)
print("Zastavky s prekrocenou kapacitou:",zastavka)
print("Najvacsie prekrocenie kapacity bolo o", najviac, "ludi.")