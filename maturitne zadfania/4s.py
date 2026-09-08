f = open("meteo_stanice.txt","r")
pocet_merani = sum(1 for line in f)
print("Pocet merani je:",pocet_merani)
f.seek(0)

najvys_tep = -1000000000000000000
teplota = ''
kod_st = '' 
priemer = 0
for riadok in f:
    riadok = riadok.strip()
    cast = riadok.split()
    teplota = cast[3]
    teplota = float(teplota.replace(",",".").replace("+",""))
    print("Teplota je:",teplota)
    priemer += teplota
    if teplota > najvys_tep:
        najvys_tep = teplota
        kod_st = cast[0]
print("Najvyssia teplota je:",najvys_tep,"na stanici s kodom:",kod_st)
priemer = priemer / pocet_merani
print("Priemerna teplota je:",round(priemer,2))