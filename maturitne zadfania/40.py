f = open(r"maturitne zadfania\spokojnost_1.txt", encoding = 'cp1250')
pocet_odpovedi = sum(1 for line in f)
print(pocet_odpovedi)
f.seek(0)
kladne = [0] * 24
zaporne = [0] * 24
hodinz = []
for line in f:
    line = line.strip()
    cast = line.replace(':', '').split()
    if cast[1] == "áno":
        kladne[int(cast[0][0:2]) - 1] += 1
    else:
        zaporne[int(cast[0][0:2]) - 1] += 1
    hodinz.append(int(cast[0]))

dni = [1]
h = hodinz[0]
for cas in hodinz[1:]:
    if cas < h:
        dni.append(0)
    dni[-1] += 1
    h = cas

for i in range(24):
    if kladne[i] > 0 or zaporne[i] > 0:
        print(f"Hodina: {i + 1} pocet vzjadreni: {kladne[i] + zaporne[i]}")

for i in range(len(dni)):
    print(f"V {i + 1}. dni bolo {dni[i]} vyjadrení")

print("Pocet dni je", len(dni))
f.close()