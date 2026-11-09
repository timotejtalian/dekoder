f = open("maturitne zadfania\\dekompresia_obrazka_1.txt", "r", encoding="utf-8")
rozmery = f.readline().strip()
f2 = open("maturitne zadfania\\dekompresia_obrazka_2.txt", "w", encoding="utf-8")
f2.write(rozmery + "\n")
for line in f:
    line = line.strip()
    cast = line.split()
    i = 0
    for farba in cast:
        if i % 2 == 0:
            f2.write("0" * int(farba))
            i += 1
        else:
            f2.write("1" * int(farba))
            i += 1
    f2.write("\n")
f2.close()
f.close()