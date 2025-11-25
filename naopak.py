def preklad(slovo):
    import random
    samohlasky = "aeiouáéíóúý"
    x = slovo.split()
    prelozene_slovo = []
    for slovo in x:
        preklad = ""
        for char in slovo:
            if char in samohlasky:
                preklad += char * 3
            else:
                preklad += char + random.choice("aeiouáéíóúý")
        prelozene_slovo.append(preklad)
    return " ".join(prelozene_slovo)
print(preklad("sos aaa"))

