import random
ot = int(input("Zadaj otazku: "))
stud = int(input("Zadaj studentov: "))
final = ""


if ot <= stud:
    print("Nie je dostatok otazok pre studentov.")
else:
    otazky = list(range(1, ot + 1))
    random.shuffle(otazky)
    studenti = list(range(1, stud + 1))
    random.shuffle(studenti)
    parne = [n for n in otazky if n % 2 == 0]
    neparne = [n for n in otazky if n % 2 != 0]
    parny_index = 0
    neparny_index = 0

    for i in range(stud):
        if i % 2 == 0:
            otazka = parne[parny_index]
            parny_index += 1
        else:
            otazka = neparne[neparny_index]
            neparny_index += 1

        final = str(i + 1) + ". student: " + str(studenti[i]) + " otazka: " + str(otazka)
        print(final)
    