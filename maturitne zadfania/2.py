f = open("hada.txt", "r")
f2 = open("hada2.txt", "x")

r = sum(1 for line in f)
print("Pocet riadkov je:", r)
f.seek(0)

najdlhsia_hra = 0
for riadok in f:
    riadok = riadok.strip()
    if len(riadok) > najdlhsia_hra:
        najdlhsia_hra = len(riadok)
print("Najdlhsia hra mala", najdlhsia_hra, "krokov.")
f.seek(0)

for riadok in f:
    riadok = riadok.strip()
    znak = riadok[0]
    pocet_znakov = 1
    for novy_znak in riadok[1:]:
        if novy_znak == znak:
            pocet_znakov += 1
        else:
            final = znak + " " + str(pocet_znakov) + " "
            f2.write(final)
            znak = novy_znak
            pocet_znakov = 1
    final = znak + " " + str(pocet_znakov) + " "
    f2.write(final)
    f2.write("\n")
f.close()
f2.close()
