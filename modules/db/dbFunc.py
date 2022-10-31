import sqlite3
from tkinter import messagebox

con = sqlite3.connect("cine1.db")
c = con.cursor()


def tablaPeliculas():
    c.execute(
        "CREATE TABLE IF NOT EXISTS peliculas(ID INTEGER PRIMARY KEY AutoIncrement, titulo TEXT NOT NULL UNIQUE,sinapsis TEXT NOT NULL,genero TEXT NOT NULL,duracion TEXT NOT NULL,director TEXT NOT NULL)"
    )


def data_entry(titulo, sinapsis, genero, duracion, director):
    t = titulo
    s = sinapsis
    g = genero
    d = duracion
    di = director

    c.execute(
        "INSERT OR IGNORE INTO peliculas (titulo, sinapsis, genero, duracion, director) VALUES (?, ?, ?, ?, ?)",
        (t, s, g, d, di),
    )
    con.commit()


def data_get(pelicula):
    c.execute(
        "SELECT titulo, sinapsis, genero, duracion, director FROM peliculas WHERE titulo=(?)",
        (pelicula,),
    )
    data = c.fetchone()
    t, s, g, d, di = data
    messagebox.showinfo(
        message=f"·Titulo: {t} \n·Sinapsis: {s} \n·Genero: {g} \n·Duración: {d} \n·Director: {di}",
        title="Información de la pelicula",
    )
