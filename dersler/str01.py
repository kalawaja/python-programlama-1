
cumle = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."

print(cumle.capitalize()) # Cümlenin ilk karakterini büyük yapar
print()
print(cumle.upper()) # BÜTÜN KARAKTERLERİ BÜYÜK YAPAR
print()
print(cumle.lower()) # bütün karakterleri küçük yapar
print()

print(cumle.find("is")) # Verilen kelime kaçıncı karakterden başlıyor
print()

print(cumle.replace("Lorem", "Ramazan")) # Eski ve Yeni karakter/kelimeleri yenisiyle değiştirir
print()
print(cumle.replace("Ipsum", "ilter").lower()) 
print()
print(cumle.replace("the", "ARTIKIL".lower())) # yeni kelimeyi küçük yazar
print()

print(cumle.split()) # boşluk karakterine göre cümleyi böler
print()
a = "".join(cumle) # daha önceden bölünmüş olan metni bir araya getirir
print(a)