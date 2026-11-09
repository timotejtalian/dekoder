f = open("maturitne zadfania\\ciernobiely_obrazok_1.txt", "r", encoding="utf-8")
f2 = open("maturitne zadfania\\ciernobiely_obrazok_2.txt", "w", encoding="utf-8")
rozmery = f.readline().strip()
f2.write(rozmery + "\n")
for line in f:
    line = line.strip()
    cast = [line[i:i + 2] for i in range(0, len(line), 2)]
    for dvojica in cast:
        if "a" <= dvojica <= "z":
            f2.write("1 ")
        else:
            f2.write("0 ")
    f2.write("\n")
f2.close()
f.close()