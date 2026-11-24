f = open(r"maturitne zadfania\\spokojnost_1.txt")
pocet_vyjadreni = sum(1 for line in f)
print("Pocet vyjadreni:", pocet_vyjadreni)
f.seek(0)

spokojny = [0] * 24
nespokojnost = [0] * 24
for line in f:
    line = line.replace(":","").strip()
    cast = line.split()
    if cast[1] != "nie":
        spokojny[int(cast[0][:2:])] += 1
    else:
        nespokojnost[int(cast[0][:2:])] += 1

print(f"Najviac spokojnych je {max(spokojny)} v {spokojny.index(max(spokojny))} hodine")
print(f"Najviac nespokojnych je {max(nespokojnost)} v {nespokojnost.index(max(nespokojnost))} hodine")

for i in range(24):
    if spokojny[i] != 0 or nespokojnost[i] != 0:
        print(f"Pocet percent spokojnosti v {i} hodine je {round(spokojny[i]/(spokojny[i]+nespokojnost[i]) * 100)}%")
f.close()