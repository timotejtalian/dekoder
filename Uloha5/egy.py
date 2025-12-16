# 7.
n = int(input("Zadaj cislo: "))
def zoznam_mocnin(n: int) -> list:
    z = []
    for i in range(1,n+1):
        z.append(i**2)
    return z
print(zoznam_mocnin(n))

# 8.
import math
from unittest import skip
def ludolf(n: int) -> list:
    z = []
    if n > 15:
        return "False"
    else:
        i = 0
        while i < n:
            i += 1
            z.append(round(math.pi,i))
    return z
print(ludolf(n))

# 9.
def usp(z : list) -> list:
    najvacsie_cislo = 0
    for i in range(len(z)):
        if najvacsie_cislo <= z[i]:
            najvacsie_cislo = z[i]
            z.remove(najvacsie_cislo)
            return "True" 
        else:
            return "False"
print(usp([1,5,7,9]))

# nahodny zoznam
import random
def generate(n: int) -> list:
    z = []
    for i in range(n):
        z.append(random.randint(1,100))
    return z
harom = generate(10)
print("Nahodny zoznam:",harom)

# 10.
def maxx(z: list) -> int:
    max_c = 0
    for i in range(len(z)):
        if max_c >= z[i]:
            skip
        else:
            max_c = (max_c * 0) + z[i]
    return max_c
print(maxx(harom))

# 11.
def index_min(z: list) -> int:
    min_c = z[0]
    index = 0
    for i in range(len(z)):
        if min_c <= z[i]:
            skip
        else:
            min_c = z[i]
            index = i
    return index
print(index_min(harom))

# 12.
def p_n (z: list) -> list:
    parne = []
    neparne = []
    for i in range (len(z)):
        if z [i] % 2 == 0:
            parne.append(z[i])
        else:
            neparne.append(z[i])
    return (parne, neparne)
print(p_n(harom))

# 13.
def hdonota(z: list) -> bool:
    hodnota = input("Zadaj hodnotu: ")
    for i in range(len(z)):
        if z[i] == int(hodnota):
            return True
    return False
print(hdonota([1,2,3,4,5,6,7,8,9,10]))