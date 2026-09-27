f = open("mena.txt","r")
polka = int((sum(1 for line in f))/2)
print("Pocet mien je",polka)
f.seek(0)

f2 = open("vystup.txt","w")

medz = 0
x = 0
n_meno = 0
n_priez = 0
najdlhsie_p = 0
mena = []
priez = []
for riadok in f:
    riadok = riadok.strip()
    cast = riadok.split()
    if x < polka:
        mena.append(cast[0:])
        if len(riadok.strip(" ")) > n_meno:
                najdlhsie_m = cast[0:] 
                n_meno = len(riadok.strip(" "))
        x += 1
    else:
        priez.append(cast[0:])
        if len(riadok.strip(" ")) > n_priez:
             najdlhsie_p = cast[0:]
             n_priez = len(riadok.strip(" "))
        x += 1

print("Dlzka najdlhsieho mena je",n_meno)
print("Dlzka najdlhsieho prizviska je",n_priez)

for i in range(polka):
    meno = " ".join(mena[i])
    priezvisko = " ".join(priez[i])
    f2.write(meno.ljust(n_meno + 1) + priezvisko + "\n")

f.close()
f2.close()

