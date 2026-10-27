import random
vstup = input("Zadaj tipy(6): ")
zreb = []
nase_tipy = vstup.split()
uhadnute_c = ""
f = open(r"loteria_1.txt", encoding = "utf-8")

for i in range(6):
    cislo = random.randint(0,101)
    if cislo in zreb:
        cislo = random.randint(0,101)
    else:
        zreb.append(cislo)

for x in range(len(zreb)):
    uhadnute_p = 0
    if nase_tipy[x] in zreb:
        uhadnute_p += 1
        uhadnute_c += nase_tipy[x]
print("Pocet uhadnutzch ",uhadnute_p,uhadnute_c)

hej = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}
for riadok in f:
    uhadnute_p = 0
    cast = riadok.split()
    for cislo in cast:
        if int(cislo) in zreb:
            uhadnute_p += 1
    hej[str(uhadnute_p)] += 1
print("Počty hráčov podľa počtu uhádnutých čísel:", hej)


