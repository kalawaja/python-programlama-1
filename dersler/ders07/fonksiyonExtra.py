
# 1000'in altındaki 3 ve 5'in tüm katlarının toplamını bulan python programı

def kontrol(num):
    if(num % 15 == 0):
        return True         # 15'in katı ise True döndür
    else:
        return False        # 15'in katı değilse False döndür

toplam = 0

for i in range(15, 1000):
    if(kontrol(i)):
        print(i, end=" ")   # tüm saıları yanyana yazdırır
        toplam += i

print("\nSayıların Toplamı: ", toplam)