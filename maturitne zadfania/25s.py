import random
pou = str(input("Zadaj tipy(6): "))
p_tipy = pou.split()

zreb = []
for i in range(6):
    cislo = random.randint(1,49)
    if cislo in zreb:
        cislo = random.randint(1,49)
    zreb.append(cislo)
print(zreb)

s_cislo = ""
for x in range(len(zreb)):
    spravne = 0
    if p_tipy[x] in zreb:
        spravne += 1
        s_cislo += p_tipy[x]
if spravne > 0:
    print("Spravne:",spravne,"cisla: ",s_cislo)
else:
    print("Nevyhravas")

hej = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}
f = open(r"loteria_1.txt", encoding = "utf-8")
for riadok in f:
    cast = riadok.split()
    spravne = 0
    for cislo in cast:
        if int(cislo) in zreb:
            spravne += 1
    hej[str(spravne)] += 1
print("Počty hráčov podľa počtu uhádnutých čísel:", hej)
