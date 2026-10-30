#dva typy: jedno a dvoj zlozkovy

#egy vs egy (jozo[fire][water])
#egy vs ketto (jozo[fire][water], jozo[fire][grass])
#ketto vs egy (jozo[vyberie silnejsi utok]
#ketto vs ketto (jozo[fire][grass,water](vynasobis), jozo[elektrik][water,grass](vynasobis), vyberies lepsie)

#{'Fire':{'normal': 1, 'fire': 0.5}, 'Water':{'normal': 1, 'water': 0.5}}
import json
typy = {'supereffective': 2, 'not_effective': 0.5, 'no_effect': 0, 'normale': 1}
mia = {}
dzejson = json.load(open("effectiveness.json", 'r', encoding='utf-8'))
for type1 in dzejson['supereffective']:
    mia[type1] = {}
    for type2 in dzejson['supereffective'][type1]:
        mia[type1][type2] = typy['supereffective']


for type1 in dzejson['not_effective']:
    for type2 in dzejson['not_effective'][type1]:
        mia[type1][type2] = typy['not_effective']
        

for type1 in dzejson['no_effect']:
    for type2 in dzejson['no_effect'][type1]:
        mia[type1][type2] = typy['no_effect']
        
 
for type1 in dzejson['normale']:
    for type2 in dzejson['normale'][type1]:
        mia[type1][type2] = typy['normale']


def vs (utoktyp: str, orbanatyp: str) -> float:
    utoktyp = utoktyp.capitalize()
    orbanatyp = orbanatyp.capitalize()
    
    if utoktyp in dzejson.get('supereffective', {}) and orbanatyp in dzejson['supereffective'][utoktyp]:
        return 2.0
    if utoktyp in dzejson.get('not_effective', {}) and orbanatyp in dzejson['not_effective'][utoktyp]:
        return 0.5
    if utoktyp in dzejson.get('no_effect', {}) and orbanatyp in dzejson['no_effect'][utoktyp]:
        return 0.0
    return 1.0
    

#for strenght in dzejson:
#    for attacker in dzejson[strenght]:
#        if not attacker in mia:
#            mia[attacker] = {}
#        for defender in dzejson[strenght][attacker]:
#            mia[attacker][defender] = typy[strenght]

def vypocet_utoku (my_army : list, enemy_army : list):
    bomba = 0.0
    for my_pokemon in my_army:
        majkspirit = my_pokemon.split()
        for enemy_pokemon in enemy_army:
            enemyspirit = enemy_pokemon.split()
            casovanabomba = 0
            for majkpyrit in majkspirit:
                terazbomba = 1.0
                for enemypyrit in enemyspirit:
                    terazbomba *= vs(majkpyrit, enemypyrit)
                casovabomab = max(terazbomba, casovabomab)
            bomba += casovanabomba
    return bomba

def atack(n1 : int, n2 : int, army : str) -> tuple:
    zoz_pok = army.split(',')
    my_army = zoz_pok[:n1:]
    enemy_army = zoz_pok[n1::]
    f1 = round(vypocet_utoku(my_army, enemy_army), 1)
    f2 = round(vypocet_utoku(enemy_army, my_army), 1)
    if f1 > f2:
        s = "JA"
    elif f2 > f1:
        s = "TEN DRUHY"
    else:
        s = "ROVNOST"  
    return(f1, f2, s)

print(atack(int(input("Velkost tvojej armady: ")), int(input("Velkost nepriatelovej armady: ")), str(input("Zadaj (armadu) vlastnosti pokemonov: "))))