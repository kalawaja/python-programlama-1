import sqlite3

def baglanti():
    with sqlite3.connect("filmarsivi.db") as baglan:
        imlec = baglan.cursor()
        imlec.execute(""" create table if not exists filmler(
                numarasi TEXT,
                adi TEXT,
                puani INT,
                fiyat FLOAT
            ) """)
        baglan.commit()
        
def ekle():
    numara = input("Film Numarası Gir: ")
    adi = input("Film Adı Gir: ")
    puan = int(input("Film Puanı Gir.: "))
    fiyat = float(input("Film Fiyatı Gir: "))
    
    with sqlite3.connect("filmarsivi.db") as baglan:
        imlec = baglan.cursor()
        imlec.execute("""
            insert into filmler values (
                "{}", "{}", {}, {}
            )""".format(numara, adi, puan, fiyat))
        baglan.commit()

def listele():
    with sqlite3.connect("filmarsivi.db") as baglan:
        imlec = baglan.cursor()
        imlec.execute("select * from filmler")
        filmler = imlec.fetchall()
        
        strCevir = lambda x: [str (y) for y in x]
        for index, film in enumerate(filmler, 1):
            print(f"{index}. {' '.join(strCevir(film))}") 
            # tuple cinsinden gelen değeri metinsel değere çevirir
 
def sil():
    listele()
    while True:
        try:
            idno = int(input("Silinecek Film Nosu Gir: "))
            break
        except Exception:
            print("Metinsel Girilemez")
    
    with sqlite3.connect("filmarsivi.db") as baglan:
        imlec = baglan.cursor()
        imlec.execute(f" delete from filmler where rowid = {idno} ")
        baglan.commit()
    listele()
        
def guncelle():
    pass
       
def main():
    guncelle()
    listele()
    """sil()
    listele()
    baglanti()
    ekle()
    
    sil()
    guncelle()"""
    
main()
    