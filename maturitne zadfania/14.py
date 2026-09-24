f = open("skosky.txt", "r")


kraj = []
for riadok in f:
    riadok = riadok.strip()
    cast = riadok.split()
    krajina = cast[1]
    prvy_vykon = cast[2]
    druhy_v = cast[3]
    treti_v = cast[4]
    stvrty_v = cast[5]
    piaty_v = cast[6]
    for i in range(0, sum(1 for line in f) + 1):
        kraj.append(krajina)
    k = list(set(kraj))
print(k)