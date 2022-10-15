from ast import arg
from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
#import PIL import ImageTk, Image

#---------------------------------------
root=Tk()
Miframe= Frame(root, width= 1280, height=720)
#------------------------------------------
.
root.title("CINEMA2000")
#root.iconbitmap("Users/clari/OneDrive/Escritorio/cc/escuela/tlp/PYTHON/proyecto tlp/logo.ico")
root.resizable(1,1)
root.config(bg="pink")

#----------------------------------------------

#------------------------------------------------------
imagenL=PhotoImage(file="./assets/images/argentina1985.png")
lbl_Imagen=Label(root, image=imagenL).place(x=50, y=10)
imagenL2=PhotoImage(file="./assets/images/avatar.png")
lbl_Imagen=Label(root, image=imagenL2).place(x=50, y=360)
imagenL3=PhotoImage(file="./assets/images/lahuerfana.png")
lbl_Imagen=Label(root, image=imagenL3).place(x=320, y=10)
imagenL4=PhotoImage(file="./assets/images/dontworrydarling.png")
lbl_Imagen=Label(root, image=imagenL4).place(x=590, y=10)
imagenL5=PhotoImage(file="./assets/images/sonrie.png")
lbl_Imagen=Label(root, image=imagenL5).place(x=850, y=10)
imagenL6=PhotoImage(file="./assets/images/blackadamn.png")
lbl_Imagen=Label(root, image=imagenL6).place(x=1100, y=10)
imagenL7=PhotoImage(file="./assets/images/thor.png")
lbl_Imagen=Label(root, image=imagenL7).place(x=320, y=360)
imagenL8=PhotoImage(file="./assets/images/losminions.png")
lbl_Imagen=Label(root, image=imagenL8).place(x=590, y=360)
imagenL9=PhotoImage(file="./assets/images/topgun.png")
lbl_Imagen=Label(root, image=imagenL9).place(x=850, y=360)
imagenL10=PhotoImage(file="./assets/images/blackpanter2.png")
lbl_Imagen=Label(root, image=imagenL10).place(x=1100, y=360)
#---------------------------------------------
def arg1985():
    messagebox.showinfo(title="ARGENTINA 1985",
        message="Durante la década de 1980, un grupo de abogados investiga y lleva a juicio a los responsables de la dictadura cívico-militar argentina.                                                                                  GENERO:Drama                                                               DURACION: 2h 20m                                                               DIRECTOR: Santiago Mitre")

def avatar():
    messagebox.showinfo(title="AVATAR 2",
        message="Jake Sully y Ney'tiri han formado una familia y hacen todo lo posible por permanecer juntos. Sin embargo, deben abandonar su hogar y explorar las regiones de Pandora cuando una antigua amenaza reaparece.                                    GENERO:Ciencia Ficcion/Aventura                                  DURACION: 166min                                                        DIRECTOR: James Cameron ")

def dontworrydarling():
    messagebox.showinfo(title="DON'T WORRY DARLING", 
    message= "Alice y Jack, todo parece ir muy bien en la vida de ambos, pero en poco tiempo, Alice descubre un proyecto de la empresa en donde trabaja Jack y él está involucrado: el misterioso Proyecto Victoria                                                                 GENERO:Suspenso                                                               DURACION: 2h 3m                                                        DIRECTORA:Olivia Wilde")

def lahuerfana():
    messagebox.showinfo(title="LA HUERFANA: EL ORIGEN", 
    message= "Lena se escapa del psiquiátrico y viaja a EE. UU. haciéndose pasar por la hija desaparecida de una familia adinerada. Pero su nueva vida como Esther no será como ella esperaba.            GENERO:Terror/Suspenso                                                           DURACION: 1h 39m                                                                 DIRECTOR: William Brent Bell")


def sonrie():
    messagebox.showinfo(title="SONRIE", 
    message="Tras la presencia de un dramático incidente sufrido por un paciente, la Dra. Cotter empieza a experimentar hechos aterradores sin explicación aparente.                                      GENERO:Terror Psicológico                                                        DURACION:1h 55m                                                              DIRECTOR: Parker Finn")

def blackadam():
    messagebox.showinfo(title="BLACK ADAM", 
    message= "Black Adam es una próxima película estadounidense de superhéroes basada en el personaje homónimo de DC Comics y pretende ser una derivación de SHAZAM!.                                 GENERO: Accion/Fantasia                                                                DURACION:2h 4m                                                     DIRECTOR:Jaume Collet-Serra")


def thor():
    messagebox.showinfo(title="THOR: AMOR Y TRUENO", 
    message="Thor está buscando la paz interior, pero la irrupción de Gorr, le obliga a volver al combate. Thor recluta a su gente para que lo ayuden a evitar la extinción de los dioses.            GENERO:Accion/Aventura                                                               DURACION: 1h 59m                                               DIRECTOR:Taika Waititi")

def losminions():
    messagebox.showinfo(title="MINIONS: NACE UN VILLANO", 
    message="En los años 70, Gru crece siendo un gran admirador de Los salvajes seis, un supergrupo de villanos. Para demostrarles que puede ser malvado, diseña un plan con la esperanza de formar parte de la banda.                                                      GENERO:Comedia                                                                          DURACION: 1h 30m                                                                 DIRECTOR: Kyle Balda")

def topgun():
    messagebox.showinfo(title="TOP GUN: MAVERICK", 
    message="Maverick, quien lleva 30 años de servicio, es ahora instructor de pilotos militares. Una última misión, Es obligado a enfrentar las heridas abiertas del pasado y sus temores más profundos.                                                                    GENERO:Accion                                                                  DURACION:2h 11m                                                          DIRECTOR:Joseph Kosinski")

def blackpanther():
    messagebox.showinfo(title="BLACK PANTHER 2: WAKANDA FOREVER", 
    message="Una secuela que seguirá explorando el incomparable mundo de Wakanda y todos los ricos y variados personajes presentados en la película de 2018.                                     GENERO:Accion                                                                DURACION:2h 41m                                                          DIRECTOR:Ryan Coogler")


#---------------------------------------------
botton_argentina=Button(root, font=("Calibri", 12, "bold"), text="▶", command=lambda:arg1985())
botton_argentina.place(x=50, y=280)  

botton_avatar=Button(root, font=("Calibri", 12, "bold"), text="▶", command=lambda:avatar())
botton_avatar.place(x=50, y=630) 

botton_dontworrydarling=Button(root, font=("Calibri", 12, "bold"), text="▶", command=lambda:dontworrydarling())
botton_dontworrydarling.place(x=590, y=280) 

botton_lahuerfana=Button(root, font=("Calibri", 12, "bold"), text="▶", command=lambda:lahuerfana())
botton_lahuerfana.place(x=320, y=280)

botton_sonrie=Button(root, font=("Calibri", 12, "bold"), text="▶", command=lambda:sonrie())
botton_sonrie.place(x=850, y=280)    

botton_blackadam=Button(root, font=("Calibri", 12, "bold"), text="▶", command=lambda:blackadam())
botton_blackadam.place(x=1100, y=280)

botton_thor=Button(root, font=("Calibri", 12, "bold"), text="▶", command=lambda:thor())
botton_thor.place(x=320, y=630)

botton_minions=Button(root, font=("Calibri", 12, "bold"), text="▶", command=lambda:losminions())
botton_minions.place(x=590, y=630) 

botton_topgun=Button(root, font=("Calibri", 12, "bold"), text="▶", command=lambda:topgun())
botton_topgun.place(x=850, y=630) 

botton_panther=Button(root, font=("Calibri", 12, "bold"), text="▶", command=lambda:blackpanther())
botton_panther.place(x=1100, y=630)
    
root.mainloop()


