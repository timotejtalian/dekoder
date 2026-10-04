import random

f_vstup = open('poprehadzovany_text1_vstup.txt', 'r', encoding='utf-8')
text = f_vstup.read()
f_vstup.close()

print('Vstupny text:')
print(text, end='\n\n')

slova = text.split()
transformovane_slova = []

for slovo in slova:
    if len(slovo) <= 3:
        transformovane_slova.append(slovo)
    else:
        pismena = list(slovo[1:-1])
        random.shuffle(pismena)
        transformovane_slova.append(slovo[0] + ''.join(pismena) + slovo[-1])

transformovany_text = ' '.join(transformovane_slova)

print('Transformovany text:')
print(transformovany_text)

f_vystup = open('poprehadzovany_text1.txt', 'w', encoding='utf-8')
f_vystup.write(transformovany_text)
f_vystup.close()
