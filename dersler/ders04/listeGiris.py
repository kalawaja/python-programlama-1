
# liste tanımlaması yapıyoruz
benimListem = ["bilgisayar", "anakart", "işlemci","ekran kartı", "harddisk"]

print(benimListem, type(benimListem))

for eleman in benimListem:
    print(eleman)

print(len(benimListem)) # liste eleman sayısını gösterme

print(benimListem[0])

harfler = list()  # list sınıfı kullanarak liste oluşturduk
for harf in benimListem[0]:  # birinci elemanın tüm karakterlerini göster
    # print(harf)
    harfler.append(harf)
print(harfler)