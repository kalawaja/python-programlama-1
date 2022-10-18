
def notGirisi():
    adSoyad = input("Öğrencinin adını ve soyadını giriniz: ")
    vize = int(input("Vize notunu giriniz: "))
    final = int(input("Final notunu giriniz: "))
    odev = int(input("Ödev notunu giriniz: "))

    with open("ogrnotlari.txt", "a", encoding="utf-8") as notlar:
        notlar.write(adSoyad + ":" + str(vize) + "-" + str(final) + "-" + str(odev) + "\n")


def menu():
    while True:
        print(""" Öğrenci Not Otomasyon Sİstemi
        1. Not Girişi 
        2. Harf Notu Listele
        3. Notları Kaydet
        4. Çıkış Yap """)

        try:
            secim = int(input("Yapmak istediğiniz işlemi seçiniz: "))
            if secim == 1:
                notGirisi()
            elif secim == 2:
                pass
            elif secim == 3:
                pass
            elif secim == 4:
                exit(0)
            else:
                print("Hatalı Değer Girildi!")

        except Exception as hata:
            print("Hatalı Değer Girildi!")
            continue
        
