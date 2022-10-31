from init import *


def data_post(titulo, sinapsis, genero, duracion, director):
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
