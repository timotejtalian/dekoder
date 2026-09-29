f = open("skosky.txt","r")

krajiny = {}
sportovci = {}
m_skok = []
for line in f:
    line = line.strip()
    cast = line.split()
    skoky = (cast[2:])
    sportovci[cast[0]] = max(skoky)
    m_skok.append(max(skoky))
    skoky = " "
    if cast[1] in krajiny:
        krajiny[cast[1]] += 1
    else:
        krajiny[cast[1]] = 1

z_kraj = []
for i in krajiny:
    z_kraj.append(i)
    print(i,":",krajiny[i])
print(",".join(z_kraj))

vytaz = []
najviac = int(max(m_skok))
for s in sportovci:
    if int(sportovci[s]) > najviac:
        vytaz.append(s)
        najviac = int(sportovci[s])
    elif int(sportovci[s]) == najviac:
            vytaz.append(s)

print(",".join(vytaz))