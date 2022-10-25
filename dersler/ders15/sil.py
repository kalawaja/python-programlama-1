import sqlite3

with sqlite3.connect("database.db") as baglanti:
    imlec = baglanti.cursor()
    imlec.execute(""" delete from sinema where fiyat = 60 """)
    imlec.execute(""" select * from sinema """)
    for kayit in imlec.fetchall():
        print(kayit)
        
    baglanti.commit()