from init import *


def tablaPeliculas():
    c.execute(
        "CREATE TABLE IF NOT EXISTS peliculas(ID INTEGER PRIMARY KEY AutoIncrement, titulo TEXT NOT NULL UNIQUE,sinapsis TEXT NOT NULL,genero TEXT NOT NULL,duracion TEXT NOT NULL,director TEXT NOT NULL)"
    )
