
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

app = Tk()
app.geometry("800x600")

def resimSec():
    dosya = askopenfilename()
    resim = ImageTk.PhotoImage(Image.open(dosya))
    foto = Label(app, image=resim)
    foto.place(x=50, y=50)

    for dosya in resimSec:
        resim = Image.open(dosya)
        resim = resim.resize((100, 100), Image.ANTIALIAS)
        resim = ImageTk.PhotoImage(resim)
        foto = Label(app, image=resim)
        foto.place(x=50, y=50)

    resimEtiket = Label(app, text="Resim Seçildi")
    resimEtiket.place(x=50, y=50)

btn = Button(app, text="Fotoğraf Seç", command=resimSec)
btn.place(x=50, y=50)

app.mainloop()