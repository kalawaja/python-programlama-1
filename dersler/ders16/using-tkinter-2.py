
import tkinter as tk

pencere = tk.Tk()
pencere.title("İkinci Windows Form Çalışması")
pencere.geometry("800x600")

adSoyad = tk.Label(pencere, text="Ad Soyad\t:")
adSoyad.place(x=100, y=10)

yas = tk.Label(pencere, text="Yaşınız\t:")
yas.place(x=100, y=40)

sifre = tk.Label(pencere, text="Şifreniz\t:")
sifre.place(x=100, y=70)

txt_adSoyad = tk.Entry(pencere, border=3, bg="white", fg="black")
txt_adSoyad.place(x=200, y=10, height=30, width=200)

txt_yas = tk.Entry(pencere, border=3, bg="white", fg="black")
txt_yas.place(x=200, y=40, height=30, width=200)

txt_Sifre = tk.Entry(pencere, border=3, bg="white", fg="black", show="*")
txt_Sifre.place(x=200, y=70, height=30, width=200)

btn_Gonder = tk.Button(pencere, border=3, text="Gönder", bg="white", fg="black", cursor="hand2")
btn_Gonder.place(x=200, y=100, height=30, width=200)

pencere.mainloop()