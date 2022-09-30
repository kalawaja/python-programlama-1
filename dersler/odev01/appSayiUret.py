
# 1 ile 100 arasında rastgele sayılar üreten python programı

"""
Sayılar random modülü ile rastgele bir değişkene atanacak,
Kullanıcıdan bir sayı girmesi istenecek,
Kullanıcı sayısı random sayıdan büyükse "Daha küçük bir sayı giriniz" uyarısı,
Kullanıcı sayısı random sayıdan küçükse "Daha büyük bir sayı giriniz" uyarısı verecek,
Kullanıcının ilk başta üç hakkı olacak.
İlk defada bilen kullanıcıya "Tebrikler ilk defada bildiniz" yazısı gösterilecek.
İkinci ve üçüncü denemede random sayıyı bilen kullanıcıya "Tebrikler Bildiniz" yazısı gösterilecek,
Üç hakkında da random sayıyı bilemeyen kullanıcıya "Bilemediniz" uyarısı ile birlikte random sayı gösterilecek,
"""

import random
randomSayi = random.randint(1,100)
print(randomSayi)
kullaniciSayi = int(input("1 ile 100 Arasında Bir Sayı Giriniz: "))

if kullaniciSayi == randomSayi:
    print("Tebrikler ilk defada bildiniz")

elif kullaniciSayi > randomSayi:
    kullaniciSayi = int(input("Daha küçük bir sayı giriniz: "))
    if kullaniciSayi > randomSayi:
        kullaniciSayi = int(input("Daha küçük bir sayı giriniz: "))
        if kullaniciSayi != randomSayi:
            print("Bilemediniz, Sayı: ", randomSayi, "olacaktı")
        else:
            print("Tebrikler Bildiniz")
else:
    kullaniciSayi = int(input("Daha büyük bir sayı giriniz: "))
    if kullaniciSayi < randomSayi:
        kullaniciSayi = int(input("Daha büyük bir sayı giriniz: "))
        if kullaniciSayi != randomSayi:
            print("Bilemediniz, Sayı: ", randomSayi, "olacaktı")
        else:
            print("Tebrikler Bildiniz")












