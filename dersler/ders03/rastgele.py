
# Rastgele sayı üreten Python programı

import random
print(round(random.random(), 3))
# 0-1 aralığında 3 ondalıklı bir tamsayı üretir
print(type(random)) # random modülünün tipini gösterir


# Rastgele Ürettiği bir sayıyı yalnızca bir kere kullanarak sayı üreten Python programı

import random
liste = []
for rnd in range(1, 30):
    sayi = random.randint(1, 30)
    if sayi not in liste:
        liste.append(sayi)
        print(sayi, end=" ")