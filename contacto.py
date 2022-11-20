from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox
#-----------------------
root=Tk()
Miframe= Frame(root, width= 1280, height=720)
#------------------------
# Tkinter config
root.title("CINEMA2000")
#root.iconbitmap("Users/clari/OneDrive/Escritorio/cc/escuela/tlp/PYTHON/proyecto tlp/logo.ico")
root.resizable(1,1)
root.config(bg="gray18")
#-----------------------------------------
#base de datos
def crear_base3():
    connection=sqlite3.connnect("cine3.db")
    return connection
#---------------------------------------------------------
#tabla
def crear_tabla3(connection):
    connection = crear_base3()
    cursor = connection.cursor()
    sql = "CREATE TABLE IF NOT EXISTS \
            contacto(\
                id INTEGER PRIMARY KEY AUTOINCREMENT,\
                    nombre TEXT NOT NULL,\
                        apellido TEXT NOT NULL,\
                            quejaconsult TEXT NOT NULL\
                              )" 
    cursor.execute(sql)
    connection.commit()
#-----------------------------
#Funciones
def funcion_c():
    conexion = crear_base3()
    cursor = conexion.cursor()
    sql = "SELECT * FROM contacto ORDER BY id DESC"
    cursor.execute(sql)
    for item in tree.get_children():
        tree.delete(item)
    tree.grid(column=0, row=2, columnspan=5, sticky="nsew")
    for row in cursor:
        tree.insert("", index=0, text=row[0], values=(row[1], row[2], row[3])),

    conexion.commit()

def FieldCleaning():
    var_nombre.set("")
    var_apellido.set("")
    var_consultquej.set("")
    funcion_c()

def Enviar_CQ(nombre, apellido, consultquej):
    nombre=entry_nombre.get()
    apellido=entry_apellido.get()
    consultquej=entry_consultaqueja.get()
    conexion = crear_base3()
    cursor = conexion.cursor()
    data = (nombre, apellido, consultquej)
    sql = "INSERT INTO contacto(nombre, apellido, consultquej) VALUES(?, ?, ?)"
    try:
        cursor.execute(sql, data) 
        conexion.commit()  
        funcion_c()
        messagebox.showinfo(title="Consulta/Queja", message=f"La consulta/queja de {nombre} {apellido} fue enviada correctamente",)
        FieldCleaning()
    except:
            messagebox.showerror(title="Error", message="Se ha producido un error, revise!")

#-----------------------------
#variables
var_id=IntVar()
miId=IntVar()
miNombre=StringVar()
var_nombre=StringVar()
miApellido=StringVar()
var_apellido=StringVar()
miConsultQuej=StringVar()
var_consultquej=StringVar()
#---------------------------------
#TreeView
tree = ttk.Treeview(root) 
tree["columns"] = ("nombre", "apellido", "consulta/queja")
tree.column("#0", width=100, minwidth=95, anchor=CENTER)
tree.column("nombre", width=100, minwidth=95, anchor=CENTER)
tree.column("apellido", width=100, minwidth=95, anchor=CENTER)
tree.column("consulta/queja", width=150, minwidth=140, anchor=CENTER)
tree.heading("#0", text="ID")
tree.heading("nombre", text="Nombre")
tree.heading("apellido", text="Apellido")
tree.heading("consulta/queja", text="Consulta/Queja")
tree.place(x=450, y=30)

#-------------------------------------
#Entries
entry_nombre = Entry(root, textvariable = var_nombre, width=50)
entry_nombre.config(fg="black", justify="center")
entry_nombre.place(x=530, y=300)
entry_apellido = Entry(root, textvariable = var_apellido, width=50)
entry_apellido.config(fg="black", justify="center")
entry_apellido.place(x=530, y=400)
entry_consultaqueja = Entry(root, textvariable = var_consultquej, width=50)
entry_consultaqueja.config(fg="black", justify="center")
entry_consultaqueja.place(x=530, y=500)
#-----------------------------
#labels
titulo = Label(root, text="DEJANOS SABER TU OPINON, CONSULTA O QUEJA", bg="white", fg="black", height=0, width=151, font=("Times New Roman", 12, "bold"))
titulo.grid(row=0, column=0, columnspan=8, padx=1, pady=1, sticky=W + E)
nombre = Label(root, text="Nombre", bg="white", fg="black", font=("Times New Roman", 12, "bold"))
nombre.place(x=350, y=298)
apellido = Label(root, text="Apellido", bg="white", fg="black", font=("Times New Roman", 12, "bold"))
apellido.place(x=350, y=400)
consultquej = Label(root, text="Consulta/Queja", bg="white", fg="black", font=("Times New Roman", 12, "bold"))
consultquej.place(x=350, y=500)

#--------------------------
#botones
boton_enviar = Button(
    root, bg= "white",
    text="Enviar", font=("Times New Roman", 12, "bold"),
    command=lambda:Enviar_CQ(var_nombre.get(), var_apellido.get(), var_consultquej.get()))
boton_enviar.place(x=950, y=390)
#--------------------

root.mainloop()
