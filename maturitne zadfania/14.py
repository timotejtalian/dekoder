f = open("skosky.txt", "r")

sportovci = {}
krajiny = {}

for riadok in f:
    riadok = riadok.strip()
    cast = riadok.split()
    
    meno = cast[0]
    krajina = cast[1]
    skoky = list(map(int, cast[2:]))

    sportovci[meno] = max(skoky)

    if krajina in krajiny:
        krajiny[krajina] += 1
    else:
        krajiny[krajina] = 1

print("Krajiny a počet športovcov:")
for krajina in krajiny:
    print(krajina, krajiny[krajina])

naj_skok = 0
vitaz = []

for meno in sportovci:
    if sportovci[meno] > naj_skok:
        naj_skok = sportovci[meno]
        vitez = [meno]
    elif sportovci[meno] == naj_skok:
        vitez.append(meno)

print("Najvyšší skok má:")
for meno in vitez:
    print(meno)
