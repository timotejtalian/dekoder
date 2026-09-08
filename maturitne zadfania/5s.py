f = open("objednane_jedla.txt","r")

pocet_jedal = sum(1 for line in f)
print("Pocet objednavok: ",pocet_jedal)
f.seek(0)

subor = f.read()
pocet_o = subor.count("o")
print("Pocet objednavok s jedlom o: ",pocet_o)
pocet_z = subor.count("z")
print("Pocet objednavok s jedlom z: ",pocet_z)
pocet_m = subor.count("m")
print("Pocet objednavok s jedlom m: ",pocet_m)
pocet_c = subor.count("c")
print("Pocet objednavok s jedlom c: ",pocet_c)

malo_jedla = ""
if pocet_o < 20:
    malo_jedla += "o, "
if pocet_z < 20:
    malo_jedla += "z, "
if pocet_m < 20:
    malo_jedla += "m, "
if pocet_c < 20:
    malo_jedla += "c "
if malo_jedla != "":
    print("Malo objednavok: ", malo_jedla)
else:
    print("Dostatok objednavok")

f.close()
