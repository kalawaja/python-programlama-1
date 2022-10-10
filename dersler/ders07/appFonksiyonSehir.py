
# Şehrin son harfi ile başlayan şehirlerin listesi

"""
1. sırayla iki şehir girilir
2. eğer girilen şehirler aynıysa yeni şehir girilir
3. girilen şehirler aynı değilse girilen şehirlerin son harfi ile başlayan şehirlerin listesi döndürülür
"""

def karsilastir(a, b):
    while (a == b):
        yenisehir = input("Yeni şehir giriniz: ")
        return yenisehir

def kontrol(sehir):
    sehirler = ["İstanbul", "Ankara", "İzmir", "Bursa", "Adana", "Antalya", "Konya", "Kayseri", "Eskişehir", "Diyarbakır", "Gaziantep", "Mersin", "Samsun", "Kocaeli", "Hatay", "Malatya", "Erzurum", "Kahramanmaraş", "Sivas", "Giresun", "Denizli", "Trabzon", "Aydın", "Tekirdağ", "Bursa", "Elazığ", "Balıkesir", "Kütahya"]

    sonharf = sehir[-1]
    sonharf = sonharf.upper()

    for i in sehirler:
        if (i[0] == sonharf):
            print(i)

sehir1 = input("Birinci şehir: ")
sehir2 = input("İkinci şehir: ")

sehir1 = karsilastir(sehir1, sehir2)
sehir2 = karsilastir(sehir2, sehir1)

kontrol(sehir1)
kontrol(sehir2)

