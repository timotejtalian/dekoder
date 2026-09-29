f = open("mena.txt","r")
polka = int(sum(1 for line in f)/2)

krstne = []
priez = []
x = 0
f.seek(0)
for line in f:
    line = line.strip()
    if x < polka:
        krstne.append(line)
        x += 1
    else:
        priez.append(line)
        x += 1
f.close()
max_meno = 0
for i in krstne:
    max_meno = max(max_meno, len(i))
print("Najdlhsie meno ma ",max_meno)

dlzka = 0
for i in priez:
    dlzka = max(dlzka, len(i))
print("Najdlhsie priezvisko ma ",dlzka)

f2 = open("vystup.txt","w")
for s in range(polka):
    f2.write(krstne[s] + " " * (max_meno - len(krstne[s]) + 1) + priez[s] + "\n")
f2.close()

