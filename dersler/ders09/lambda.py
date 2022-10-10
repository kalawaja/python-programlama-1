
# lambda fonksiyonları, tek satırlık fonksiyonlar oluşturmak için kullanılır.
# lambda fonksiyonları, isimsiz fonksiyonlardır.
# lambda fonksiyonları, bir değişkene atanabilir.
# lambda fonksiyonları, bir fonksiyonun parametresi olarak kullanılabilir.
# lambda fonksiyonları, bir fonksiyonun dönüş değeri olarak kullanılabilir.
# lambda fonksiyonları, bir fonksiyonun içinde kullanılabilir.
# lambda fonksiyonları, bir fonksiyonun içinde tanımlanabilir.
# lambda fonksiyonları, bir fonksiyonun içinde çağrılabilir.
# lambda fonksiyonları, bir fonksiyonun içinde return edilebilir.

"""Lambda fonksiyon tanımlanırken amacı: tek satırda işlemleri yapan fonksiyondur.
Lambda içine değer gönderirken parantez içine arguman isimleri yazılarak çağırılır, return ile print kullanılarak yazdırılabilir."""


# Toplama işlemi yapan lambda fonksiyonu;

topla = lambda s1,s2: s1 + s2

s1 = int(input("1. Sayı: "))
s2 = int(input("2. Sayı: "))

print(topla(s1, s2))

"""
# Küp Alma Fonksiyonu;

def kup(s1):
    return lambda : s1 ** 3

s1 = int(input("Sayı Giriniz: "))
print("Küp: ", kup(s1)())"""

"""
# Tam Bölme ve Kalan Bulma Fonksiyonu;

def tamBolme(s1, s2):
    return lambda : s1 // s2

def kalanBul(s1, s2):
    return lambda : s1 % s2

s1 = int(input("1. Sayı: "))
s2 = int(input("2. Sayı: "))
print("Tam Bölüm: ", tamBolme(s1, s2)())
print("Kalan: ", kalanBul(s1, s2)())"""



