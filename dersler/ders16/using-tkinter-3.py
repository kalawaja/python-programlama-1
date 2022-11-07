
# Adınız, Soyadınız, Ara Sınav Notunuz, Final Notunuz, Hesapla butonu

import tkinter as tk

pencere = tk.Tk()

pencere.title("Sınav Not Hesaplama")

pencere.geometry("600x600")

ad = tk.Label(pencere, text="Adınız\t:")
ad.place(x=100, y=10)

soyad = tk.Label(pencere, text="Soyadınız\t:")
soyad.place(x=100, y=40)

arasinav = tk.Label(pencere, text="Ara Sınav Notunuz\t:")
arasinav.place(x=100, y=70)

final = tk.Label(pencere, text="Final Notunuz\t:")
final.place(x=100, y=100)

txt_ad = tk.Entry(pencere, border=3, bg="white", fg="black")
txt_ad.place(x=300, y=10, height=30, width=200)

txt_soyad = tk.Entry(pencere, border=3, bg="white", fg="black")
txt_soyad.place(x=300, y=40, height=30, width=200)

txt_arasinav = tk.Entry(pencere, border=3, bg="white", fg="black")
txt_arasinav.place(x=300, y=70, height=30, width=200)

txt_final = tk.Entry(pencere, border=3, bg="white", fg="black")
txt_final.place(x=300, y=100, height=30, width=200)

# Ara Sınav Notu + Final Notu / 2

def hesapla():
    arasinav = int(txt_arasinav.get())
    final = int(txt_final.get())
    ortalama = (arasinav + final) / 2
    not_ortalama = tk.Label(pencere, text="Ortalamanız\t:" + str(ortalama))
    not_ortalama.place(x=300, y=190)

def temizle():
    txt_ad.delete(0, tk.END)
    txt_soyad.delete(0, tk.END)
    txt_arasinav.delete(0, tk.END)
    txt_final.delete(0, tk.END)
    

btn_hesapla = tk.Button(pencere, border=3, text="Hesapla", bg="white", fg="black", cursor="hand2", command=hesapla)

btn_hesapla.place(x=300, y=130, height=30, width=200)

btn_temizle = tk.Button(pencere, border=3, text="Temizle", bg="white", fg="black", cursor="hand2", command=temizle)

btn_temizle.place(x=300, y=160, height=30, width=200)

pencere.mainloop()