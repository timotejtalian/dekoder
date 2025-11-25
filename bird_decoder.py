def preklad(slovo):
    samohlasky = "aeiouáéíóúý"
    prelozene_slovo = []
    x = slovo.split()
    for s in x:
        index = 0
        preklad = ""
        while index < len(s):
            if s[index] in samohlasky:
                preklad += s[index]
                index += 3
            else:
                preklad += s[index]
                index += 2
        prelozene_slovo.append(preklad)
    return " ".join(prelozene_slovo)
print(preklad("hieeelalaooo"))
