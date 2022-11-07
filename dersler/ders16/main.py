
# Tkinter Kullanımı

import tkinter
w=input("Genişlik değeri giriniz: ")
h=input("Yükseklik değeri giriniz: ")
print()
x=int(input("Yatay konumu giriniz: "))
y=int(input("Dikey konumu giriniz: "))
pencere = tkinter.Tk()
pencere.title("İlk Windows Form Çalışması")
pencere.iconbitmap("python-icon.ico")

pencere.geometry(w+"x"+h+"+"+str(x)+"+"+str(y))
pencere.config(bg="black")
pencere.maxsize(800,800)
pencere.minsize(200,200)

pencere.resizable(False,True)

pencere.mainloop()