
# Dosyalama İşlemlerinde Okuma ve Yazma Modu olarak 2 farklı mod vardır.
# Okuma modu: r
# Yazma modu: w
# Okuma ve yazma modu: r+
# Yazma ve okuma modu: w+
# Okuma ve ekleme modu: a
# Okuma ve ekleme modu: a+

# encoding="utf-8" dosyaların içerisindeki Türkçe karakterlerin okunmasını sağlar.

# open() fonksiyonu ile dosya açılır.
# read() fonksiyonu ile dosya okunur.
# write() fonksiyonu ile dosyaya yazılır.
# close() fonksiyonu ile dosya kapatılır.
# seek() fonksiyonu ile dosya konumu değiştirilir.
# tell() fonksiyonu ile dosya konumu öğrenilir.
# flush() fonksiyonu ile dosya belleğe yazılır.
# fileno() fonksiyonu ile dosya numarası öğrenilir.

# Dosya konumu öğrenme/değiştirme işlemleri:
# 0: Dosyanın başlangıcı
# 1: Dosyanın bulunduğu konum
# 2: Dosyanın sonu

"""dosya = open("deneme.txt", "r", encoding="utf-8")
oku = dosya.read()
print(oku)
dosya.close()"""

try:
    with open("python-programlama-1/dersler/ders12/file-read/deneme.txt", "r", encoding="utf-8") as dosya:
        oku = dosya.read()
        print(oku)
except Exception as hata:
    print(hata)