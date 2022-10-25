import sqlite3

with sqlite3.connect("database.db") as baglanti:
    imlec = baglanti.cursor()
    imlec.execute(""" update sinema set turu = "fantastik" where filmadi = "yenilmezler" """)
    imlec.execute(""" update sinema set fiyat = 80 where turu = "macera" """)
    
    # set ile yeni değer where ile varolan değer girişi yapılır
    baglanti.commit()