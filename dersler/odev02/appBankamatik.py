
# Ödev 2 - Bankamatik (ATM) Uygulaması

"""Ödev 2 - Bankamatik (ATM) Uygulaması

Kullanıcı, çekmek istediği miktarı yazar.
(Kağıt para olarak çıktı alınacak.)
Örnek: 1453 TL para çekmek isteniyorsa önce en yüksek miktardan bölme yapılacak ve çekilen tutar kalandan düşülecek; 
(1453/200 = 7 adet 200 TL) → Kalan 53
(53/50 = 1 adet 50 TL) → Kalan 3
(3 adet 1 TL bozuk para)
(Diğer miktarlar varsa onları da yazdırabilirsiniz.)"""

# Çözüm

# 1. Adım: Müşteriden para çekme miktarını al.
# 2. Adım: Para çekme miktarını 200, 100, 50, 20, 10, 5, 1 TL'ye böl.
# 3. Adım: Bölüm sonuçlarını ekrana yazdır. (Kaç tane kaçlık!)
# 4. Adım: Dekont yazdırmak isteyip istemediğini sor.
# 5. Adım: Dekontu yazdır (veya işlemi sonlandır.)

miktar = int(input("Para çekmek istediğiniz miktarı giriniz: "))
print("Para çekme miktarı:", miktar)

bolum = miktar // 200  # İlk bölüm; miktarın 200'e bölümüdür. (7)
kalan = miktar % 200   # İlk kalan; miktarın 200'e bölümünden kalanıdır.(53)
print("200 TL:", bolum)

bolum = kalan // 100   # kalanın bölümü (0)
kalan = kalan % 100    # kalanın kalanı (53)
print("100 TL:", bolum)

bolum = kalan // 50     # kalanın bölümü (1)
kalan = kalan % 50      # kalanın kalanı (3)
print("50 TL:", bolum)

bolum = kalan // 20     # kalanın bölümü (0)
kalan = kalan % 20      # kalanın kalanı (3)
print("20 TL:", bolum)

bolum = kalan // 10     # kalanın bölümü (0)
kalan = kalan % 10      # kalanın kalanı (3)
print("10 TL:", bolum)

bolum = kalan // 5      # kalanın bölümü (0)
kalan = kalan % 5       # kalanın kalanı (3)
print("5 TL:", bolum)

bolum = kalan // 1      # kalanın bölümü (3)
kalan = kalan % 1       # kalanın kalanı (0)
print("1 TL:", bolum)

print("Para çekme işlemi tamamlandı.")

dekont = str(input("Dekont yazdırmak istiyor musunuz? (E/H): "))
if dekont == "E":
    print("Dekont yazdırılıyor...")
    print("Dekont yazdırıldı.")
else:
    print("Dekont yazdırılmadı.")