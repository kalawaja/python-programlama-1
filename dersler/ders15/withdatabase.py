import sqlite3

with sqlite3.connect("database.db") as baglanti:
    imlec = baglanti.cursor()
    imlec.execute("select * from sinema")
    
    for kayit in imlec.fetchall(): # tablo içindeki kayıtları print ile yazdır
        if kayit[4] > 50:
            print(f"Sinema Adı {kayit[1]} \t Fiyatı {kayit[4]}")
            # print(kayit[1])
        
    baglanti.commit()