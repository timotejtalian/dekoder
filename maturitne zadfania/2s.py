f = open("hada.txt","r")
f2 = open("hada3.txt","x")

pocet_h = sum(1 for line in f)
print("Pocet hier: ", pocet_h)
f.seek(0)

najdlhsia = 0
znak = ""
pocet_znakov = 1
for riadok in f:
    riadok = riadok.strip()
    if len(riadok) > najdlhsia:
        najdlhsia = len(riadok)
    print("Najdlhsia hra mala",najdlhsia,"krokov.")
    znak = riadok[0]
    for novy_znak in riadok[1:]:
        if znak == novy_znak:
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