f = open("objednane_jedla.txt", "r")
pocet_objednavok = sum(1 for line in f)
print (pocet_objednavok)
f.seek(0)

subor = f.read()
pocet_o = subor.count("o")
pocet_z = subor.count("z")
pocet_m = subor.count("m")
pocet_c = subor.count("c")
print("Oranzova:", pocet_o)
print("Modra:", pocet_m)
print("Cervena:", pocet_c)
print("Zelena:", pocet_z)
malo_jedla = ""
if pocet_o < 20:
    malo_jedla += "o "
if pocet_z < 20:
    malo_jedla += "z "
if pocet_m < 20:
    malo_jedla += "m " 
if pocet_c < 20:
    malo_jedla += "c"
if malo_jedla != "":
    print("Malo objednavok:", malo_jedla)
else:
    print("Dostatok objednavok")
f.seek(0)
f.close()
