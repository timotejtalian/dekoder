vstup = open("maturitne zadfania\\hlasovanie_2.txt", "r", encoding="utf-8")
f1 = open("maturitne zadfania\\5221.txt", "w", encoding="utf-8")
f2 = open("maturitne zadfania\\5222.txt", "w", encoding="utf-8")
f3 = open("maturitne zadfania\\5223.txt", "w", encoding="utf-8")
f4 = open("maturitne zadfania\\5224.txt", "w", encoding="utf-8")
f5 = open("maturitne zadfania\\5225.txt", "w", encoding="utf-8")
f6 = open("maturitne zadfania\\5226.txt", "w", encoding="utf-8")
f7 = open("maturitne zadfania\\5227.txt", "w", encoding="utf-8")
f8 = open("maturitne zadfania\\5228.txt", "w", encoding="utf-8")
f9 = open("maturitne zadfania\\5229.txt", "w", encoding="utf-8")
pocet_SMS = sum(1 for line in vstup)
print("Počet SMS správ: ", pocet_SMS)
i = 0
vstup.seek(0)
for line in vstup:
    line = line.strip()
    cast = line.split(";")
    if cast[0] == "5221":
        f1.write(str(i) + "\n")
    elif cast[0] == "5222":
        f2.write(str(i) + "\n")
    elif cast[0] == "5223":
        f3.write(str(i) + "\n")
    elif cast[0] == "5224":
        f4.write(str(i) + "\n")
    elif cast[0] == "5225":
        f5.write(str(i) + "\n")
    elif cast[0] == "5226":
        f6.write(str(i) + "\n")
    elif cast[0] == "5227":
        f7.write(str(i) + "\n")
    elif cast[0] == "5228":
        f8.write(str(i) + "\n")
    elif cast[0] == "5229":
        f9.write(str(i) + "\n")
    i += 1
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
f8.close()
f9.close()
vstup.close()