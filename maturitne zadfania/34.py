f = open("maturitne zadfania\\dekompresia_obrazka_1.txt", "r", encoding="utf-8")
rozmery = f.readline().strip()
f2 = open("maturitne zadfania\\dekompresia_obrazka_2.txt", "w", encoding="utf-8")
f2.write(rozmery + "\n")
for line in f:
    i = 0
    line = line.strip()
    cast = line.split()
    for farba in cast:
        if i % 2 == 0:
            f2.write(int(farba)*"0")
            i += 1
        else:
            f2.write(int(farba)*'1')
            i += 1
    f2.write("\n")
f2.close()
f.close()