
# form üzerine fotoğraf ekleme
# pip pillow; fotoğraf işlemleri

from tkinter import *
from PIL import Image, ImageTk

app = Tk()
app.geometry("800x600")
resim = ImageTk.PhotoImage(Image.open("bg.jpg"))
foto = Label(app, image=resim)
foto.place(x=50, y=50)

app.mainloop()


