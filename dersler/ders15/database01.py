import sqlite3

baglanti = sqlite3.connect("database.accdb")  # veritabanı oluşturulur
imlec = baglanti.cursor()  # veritabanı içinde dolaşabileceğimiz bir cursor oluşturulur
imlec.execute(""" 
                create table if not exists sinema (filmkodu TEXT, filmadi TEXT, puani INT, turu TEXT, fiyat INT, cikistarihi DATE, vizyondami BOOL)
              """)

imlec.execute(""" insert into sinema values ("A15", "spider man", 10, "macera", 70, "10.05.2019", 1) """)

baglanti.commit()  # yukarıdaki sql sorgusunu onaylarsınız
baglanti.close()   # bağlantıyı kapatırız