import random
f = open("poprehadzovany_text_vstup2.txt", "r", encoding="utf-8")
text = f.read()
f.close()

print('Vstupny text:')
print(text, end='\n\n')

slova = text.split()
transformovane_slova = []
for slovo in slova:
    if len(slovo) <= 3:
            transformovane_slova.append(slovo)
    else:
        if slovo[0].isalpha() and slovo[-1].isalpha():
            pismena = list(slovo[1:-1])
            random.shuffle(pismena)
            transformovane_slova.append(slovo[0] + ''.join(pismena) + slovo[-1])
        elif not slovo[0].isalpha():
            pismena = list(slovo[2:-1])
            random.shuffle(pismena)
            transformovane_slova.append(slovo[0:2] + ''.join(pismena) + slovo[-1])
        elif not slovo[-1].isalpha():
            pismena = list(slovo[1:-2])
            random.shuffle(pismena)
            transformovane_slova.append(slovo[0] + ''.join(pismena) + slovo[-2] + slovo[-1])
transformovany_text = ' '.join(transformovane_slova)

print('Transformovany text:')
print(transformovany_text)

f_vystup = open('poprehadzovany_text2.txt', 'w', encoding='utf-8')
f_vystup.write(transformovany_text)
f_vystup.close()
