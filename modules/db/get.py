from init import *


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
