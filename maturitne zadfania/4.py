f = open("meteo_stanice.txt", "r")
pocet_merani = sum(1 for line in f)
print("Pocet merani:", pocet_merani)
f.seek(0)

teplota = " "
najvys_tep = -1000
kod_st = " "
priemer = 0
for riadok in f:
    riadok = riadok.strip()
    casti = riadok.split()
    teplota = (casti[3])
    teplota = teplota.replace(",", ".").replace("+", "")
    teplota = float(teplota)
    priemer += teplota
    print("Teplota:", teplota)
    if teplota > najvys_tep:
        najvys_tep = teplota
        kod_st = casti[0]
priemer = priemer / pocet_merani
print("Priemerna teplota je:", round(priemer, 2))
print("Najvyssia teplota je:", najvys_tep, "Kod stanice:", kod_st)
f.close()
