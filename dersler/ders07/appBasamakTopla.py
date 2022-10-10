
# Herhangi bir sayı üssünün basamakları toplamındaki sayılar kaçtır?

# 1. Herhangi bir taban sayısı gir 
# 2. Girilen sayının üs değerini gir
# 3. Üssün basamakları toplamı kaçtır?

"""def basamakTopla(num):
    toplam = 0
    while (num > 0):
        toplam += num % 10
        num //= 10
    return toplam

taban = int(input("Taban sayısı: "))
us = int(input("Üs değeri: "))
sayi = taban ** us

print("Sayının basamakları toplamı: ", basamakTopla(sayi))"""

# 2. Yöntem

"""def basamakTopla(num):
    toplam = 0
    for i in str(num):
        toplam += int(i)
    return toplam

taban = int(input("Taban sayısı: "))
us = int(input("Üs değeri: "))
sayi = taban ** us

print("Sayının basamakları toplamı: ", basamakTopla(sayi))"""

# 3. Yöntem

def basamakToplami(us):
    taban = int(input("Taban sayısı Giriniz: "))
    sayi = taban ** us
    toplam = 0

    for rakam in str(sayi):
        toplam += int(rakam)
    print("Girilen Sayı: ", sayi)
    return toplam

uslu = int(input("Üs değeri Giriniz: "))
superToplam = basamakToplami(uslu)
print("Basamakların Toplamı: ", superToplam)

