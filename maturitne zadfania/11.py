f = open("maturitne zadfania\\sportovci.txt", "r")
pocet_sportovcov = sum(1 for line in f)
print("Pocet sportovcov: ", pocet_sportovcov)
f.seek(0)

najlepsi = ""
najrychlejsi_cas = 1000000000000000000000000000000000000000000000000000000000000000000000000000000
for riadok in f:
    riadok = riadok.strip()
    cast = riadok.split()
    print("Sutaziaci ",cast[0], "dobehol do ciela za", cast[1], "sekund.")
    if int(cast[1]) < najrychlejsi_cas:
        najrychlejsi_cas = int(cast[1])
        najlepsi = cast[0]
    min, sek = divmod(najrychlejsi_cas, 60)
print("Najrychlejsi cas: ", min, "min. ", sek, "sek. Dosiahol ho sutaziaci: ", najlepsi)