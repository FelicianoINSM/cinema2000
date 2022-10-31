# Imports
from tkinter import *
import modules.db.dbFunc
from modules.movies import hardcode_upload


# ------------------------------------------

# Window config

root = Tk()
Miframe = Frame(root, width=1280, height=720)

# ------------------------------------------

# Tkinter config

root.title("CINEMA2000")
# root.iconbitmap("Users/clari/OneDrive/Escritorio/cc/escuela/tlp/PYTHON/proyecto tlp/logo.ico")
root.resizable(1, 1)
root.config(bg="pink")
# -----------------------------------------

# Base de datos

modules.db.dbFunc.tablaPeliculas()
hardcode_upload()

# -----------------------------------------

# Images load

imagenL = PhotoImage(file="./assets/images/argentina1985.png")
lbl_Imagen = Label(root, image=imagenL).place(x=50, y=10)
imagenL2 = PhotoImage(file="./assets/images/avatar.png")
lbl_Imagen = Label(root, image=imagenL2).place(x=50, y=360)
imagenL3 = PhotoImage(file="./assets/images/lahuerfana.png")
lbl_Imagen = Label(root, image=imagenL3).place(x=320, y=10)
imagenL4 = PhotoImage(file="./assets/images/dontworrydarling.png")
lbl_Imagen = Label(root, image=imagenL4).place(x=590, y=10)
imagenL5 = PhotoImage(file="./assets/images/sonrie.png")
lbl_Imagen = Label(root, image=imagenL5).place(x=850, y=10)
imagenL6 = PhotoImage(file="./assets/images/blackadamn.png")
lbl_Imagen = Label(root, image=imagenL6).place(x=1100, y=10)
imagenL7 = PhotoImage(file="./assets/images/thor.png")
lbl_Imagen = Label(root, image=imagenL7).place(x=320, y=360)
imagenL8 = PhotoImage(file="./assets/images/losminions.png")
lbl_Imagen = Label(root, image=imagenL8).place(x=590, y=360)
imagenL9 = PhotoImage(file="./assets/images/topgun.png")
lbl_Imagen = Label(root, image=imagenL9).place(x=850, y=360)
imagenL10 = PhotoImage(file="./assets/images/blackpanter2.png")
lbl_Imagen = Label(root, image=imagenL10).place(x=1100, y=360)

# ------------------------------------------

# Buttons

button_argentina = Button(
    root,
    font=("Calibri", 12, "bold"),
    text="▶",
    command=lambda: modules.db.dbFunc.data_get("ARGENTINA 1985"),
)
button_argentina.place(x=50, y=280)

button_avatar = Button(
    root,
    font=("Calibri", 12, "bold"),
    text="▶",
    command=lambda: modules.db.dbFunc.data_get("AVATAR 2"),
)
button_avatar.place(x=50, y=630)

button_dontworrydarling = Button(
    root,
    font=("Calibri", 12, "bold"),
    text="▶",
    command=lambda: modules.db.dbFunc.data_get("DON'T WORRY DARLING"),
)
button_dontworrydarling.place(x=590, y=280)

button_lahuerfana = Button(
    root,
    font=("Calibri", 12, "bold"),
    text="▶",
    command=lambda: modules.db.dbFunc.data_get("LA HUERFANA: EL ORIGEN"),
)
button_lahuerfana.place(x=320, y=280)

button_sonrie = Button(
    root,
    font=("Calibri", 12, "bold"),
    text="▶",
    command=lambda: modules.db.dbFunc.data_get("SONRIE"),
)
button_sonrie.place(x=850, y=280)

button_blackadam = Button(
    root,
    font=("Calibri", 12, "bold"),
    text="▶",
    command=lambda: modules.db.dbFunc.data_get("BLACK ADAM"),
)
button_blackadam.place(x=1100, y=280)

button_thor = Button(
    root,
    font=("Calibri", 12, "bold"),
    text="▶",
    command=lambda: modules.db.dbFunc.data_get("THOR: AMOR Y TRUENO"),
)
button_thor.place(x=320, y=630)

button_minions = Button(
    root,
    font=("Calibri", 12, "bold"),
    text="▶",
    command=lambda: modules.db.dbFunc.data_get("MINIONS: NACE UN VILLANO"),
)
button_minions.place(x=590, y=630)

button_topgun = Button(
    root,
    font=("Calibri", 12, "bold"),
    text="▶",
    command=lambda: modules.db.dbFunc.data_get("TOP GUN: MAVERICK"),
)
button_topgun.place(x=850, y=630)

button_panther = Button(
    root,
    font=("Calibri", 12, "bold"),
    text="▶",
    command=lambda: modules.db.dbFunc.data_get("BLACK PANTHER 2: WAKANDA FOREVER"),
)
button_panther.place(x=1100, y=630)

# ------------------------------------------

root.mainloop()
