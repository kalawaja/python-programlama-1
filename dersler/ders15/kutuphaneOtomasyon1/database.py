import sqlite3, main

def baglanti():     # database oluşturma
    baglan = sqlite3.connect("BenimKutuphanem.db")
    imlec = baglan.cursor()
    imlec.execute("create table if not exists tbl_kitaplar(ad TEXT, yazar TEXT, turu TEXT, fiyat FLOAT, stoktaMi BOOL)")
    baglan.commit()
    baglan.close()

def ekle():     # kayıt ekleme
    with sqlite3.connect("BenimKutuphanem.db") as baglanti:
        imlec = baglanti.cursor()  
        
        imlec.execute("""insert into tbl_kitaplar values("{}","{}","{}","{}","{}")""".format(main.kutuphane1.ad, main.kutuphane1.yazar, main.kutuphane1.turu, main.kutuphane1.fiyat, main.kutuphane1.stoktaMi))
        baglanti.commit()
    

def sil():
    with sqlite3.connect("BenimKutuphanem.db") as baglanti:
        imlec = baglanti.cursor()
        
        imlec.execute("select * from tbl_kitaplar")
        kitaplar = imlec.fetchall()
        
        strCevir = lambda x: [str (y) for y in x]
        for i, j in enumerate(kitaplar, 1):
            print("{}- {}".format(i, " ".join(strCevir(j))))

        while True:
            try:
                sec = int(input("Silinecek Kitap no yazın.: "))
                break
            except ValueError:
                print("Sayısal Bir Deger Girin")
                
        imlec.execute("delete from tbl_kitaplar where rowid={}".format(sec))
        
        baglanti.commit()
                
def guncelle():
    with sqlite3.connect("BenimKutuphanem.db") as baglanti:
        imlec = baglanti.cursor()
        
        imlec.execute("select * from tbl_kitaplar")
        kitaplar = imlec.fetchall()
        
        strCevir = lambda x: [str (y) for y in x]
        for i, j in enumerate(kitaplar, 1):
            print("{}- {}".format(i, " ".join(strCevir(j))))

        while True:
            try:
                sec = int(input("Guncellenecek Kitap no yazın.: "))
                break
            except ValueError:
                print("Sayısal Bir Deger Girin")
        
        while True:
            try:         
                sutunGuncelle = int(input("""Guncellenecek Sutun Seciniz
        1- AD
        2- YAZAR
        3- TURU
        4- FIYAT
        5- STOK DURUMU
Seciminiz..: """))
                if sutunGuncelle < 1 or sutunGuncelle > 5:
                    continue
                break
            except ValueError:
                print("Sayisal Deger Giriniz.")
            
        basliklar = ["ad","yazar","turu","fiyat","stoktaMi"]
        yeniDeger = input("Yeni Deger Girin.: ")
        imlec.execute("update tbl_kitaplar set {} = '{}' where rowid = {}".format(basliklar[sutunGuncelle -1], yeniDeger, sec))    

        baglanti.commit()
        
        print("\nKayıt Başarılı")
def listele():
    with sqlite3.connect("BenimKutuphanem.db") as baglanti:
        imlec = baglanti.cursor()
        
        imlec.execute("select * from tbl_kitaplar")
        kitaplar = imlec.fetchall()
        
        strCevir = lambda x: [str (y) for y in x]
        for i, j in enumerate(kitaplar, 1):
            print("{}- {}".format(i, " ".join(strCevir(j))))
        baglanti.commit()