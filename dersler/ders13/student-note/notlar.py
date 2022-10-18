

def harfNotuHesapla(ogr):  # ali:50-70-90
    ogrenci = ogr.split(":")
    ogrAdi = ogrenci[0]  # ogrencinin adsoyad bilgilerini içeriyor
    notlar = ogrenci[1].split("-")  # ogrencinin not bilgilerini içeriyor "-" den ayırdık
    
    vize = int(notlar[0])
    final = int(notlar[1])
    odev = int(notlar[2])
    
    ortalama = (odev * 0.2) + (vize * 0.3) + (final * 0.5)
    
    if(ortalama >= 85 and ortalama <=100):
        harfNotu = "AA"
    elif(ortalama >= 70 and ortalama <85):
        harfNotu = "BB"
    elif(ortalama >= 60 and ortalama <70):
        harfNotu = "CC"
    elif(ortalama >= 50 and ortalama <60):
        harfNotu = "DD"
    elif(ortalama >= 0 and ortalama <50):
        harfNotu = "FF"
    else:
        print("Gecersiz Not!")
    
    # print("ortalama:",ortalama)  # ortalamasını terminalde gosterdik
    return (ogrAdi + ": " + harfNotu)  # ogr parametresine karşılık buradaki değeri gönderdik

def harfNotuKaydet():
    try:
        # listenin amacı: harfnotu fonks gelen değerleri listede sakla ve yeni bir dosyaya yaz
        liste = []
        with open("ogrnotlari.txt", encoding="utf-8") as notlar:
            for ogrenci in notlar:
                liste.append(harfNotuHesapla(ogrenci))
            with open("harfNotlari.txt", "w", encoding="utf-8") as harfnotu:
                for i in liste:
                    harfnotu.write(i)
                    harfnotu.write("\n")
        print("Öğrenci Harf Notları Kaydedilmiştir.")
                
    except Exception as hata:
        print("Hata Oluştu", hata)

def notlariListele():
    #dosya oluşturulmamışsa hata oluştur
    try:
        with open("ogrnotlari.txt", encoding="utf-8") as notlar:
            for ogrenci in notlar:
                print(harfNotuHesapla(ogrenci))              
    except Exception as hata:
        print("Hata Oluştu", hata)


def notGirisi():
    adSoyad = input("Ad ve Soyad Girin.: ")
    vize = int(input("Vize Notunu Girin.:"))
    final = int(input("Final Notunu Girin.:"))
    odev = int(input("Ödev Notunu Girin.:"))

    with open("ogrnotlari.txt", "a", encoding="utf-8") as notlar:
        notlar.write(adSoyad + ":" + str(vize) + "-" + str(final) + "-" + str(odev) + "\n")

def menu():
    while True:
        print(""" ÖĞRENCİ NOT OTOMASYON SİSTEMİ
        1. Not Girişi
        2. Harf Notu Listele
        3. Harf Notu Kaydet 
        4. Çıkış""")
        
        try:
            secim = int(input("Seciminiz.: "))
            if (secim == 1):
                notGirisi()
            elif (secim == 2):
                notlariListele()
            elif (secim == 3):
                harfNotuKaydet()
            elif (secim == 4):
                exit(0)
            else:
                print("Hatalı Değer Girildi")

        except Exception as hata:
            print("Hatalı Deger Girildi")
            continue