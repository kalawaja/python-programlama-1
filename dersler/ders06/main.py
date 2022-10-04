
"""# fonksiyonlarim.py 'den fonksiyonlari cagiriyoruz (1.yöntem) 

from fonksiyonlarim import *

mesaj() 
s1, s2 = 10, 20
toplam(s1, s2) 
carpim(s1, s2)"""

"""# fonksiyonlarim.py 'den fonksiyonlari cagiriyoruz (2.yöntem)

import fonksiyonlarim as fn

s1, s2 = 10, 20
fn.toplam(s1, s2) 
fn.carpim(s1, s2)

fn.mesaj()"""


"""# fonksiyon.py 'den fonksiyonlari cagiriyoruz (devamı; kare işlemi için)

from fonksiyonlarim import *

mesaj() 
s1 = int(input("Taban değerini giriniz: "))
s2 = int(input("Üs değerini giriniz: "))
kare(s1, s2)"""

# faktoriyel hesaplama 

from math import factorial as fkt

def faktoriyel(sayi):
    print(fkt(sayi))

sayi = int(input("Sayıyı giriniz: "))
faktoriyel(sayi)

# lambda ile toplama, çıkarma, çarpma, bölme işlemleri

toplam = lambda sayi1, sayi2: sayi1 + sayi2
cikarma = lambda sayi1, sayi2: sayi1 - sayi2
carpma = lambda sayi1, sayi2: sayi1 * sayi2
bolme = lambda sayi1, sayi2: sayi1 / sayi2

print(toplam(10, 20))
print(cikarma(10, 20))
print(carpma(10, 20))
print(bolme(10, 20))

# lambda ile faktoriyel hesaplama

faktoriyel = lambda sayi: 1 if sayi == 0 else sayi * faktoriyel(sayi - 1)

print(faktoriyel(5))



