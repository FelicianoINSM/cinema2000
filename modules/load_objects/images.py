from tkinter import *


def load_image(path, frame, xcoor, ycoor):
    imagen = PhotoImage(file=path)
    cargar = Label(frame, image=imagen).pack(x=xcoor, y=ycoor)
