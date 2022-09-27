
ad = input("Adınızı Giriniz: ") # input; programa bilgi girişi yapar
soyad = input("Soyadınızı Giriniz: ")
yas = input("Yaşınızı Giriniz: ")
# pythonda değişken tanımlaması yapılmaz ancak tür dönüşümü yapılır

print(ad, soyad, yas)
print(ad+soyad+yas)

# print(ad+soyad+int(yas)) metinsel ifadeye sayısal ifade eklenince tip hatası verir

# 10+20=30  (sayısal toplama)
# 10+20=1020 (metinsel toplama)

ad = input("Adınız: ")
soyad = input("Soyadınız: ")
print(type(ad), type(yas))
