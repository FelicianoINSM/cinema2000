import sqlite3

def crear_base():
    connection=sqlite3.connnect("cine1.db")
    return connection

def tableMovie(connection):
    connection = crear_base()
    cursor = connection.cursor()
    sql = "CREATE TABLE IF NOT EXISTS \
            peliculas(\
                titulo TEXT NOT NULL,\
                    sinapsis TEXT NOT NULL,\
                        genero TEXT NOT NULL,\
                            duracion TEXT NOT NULL,\
                                director TEXT NOT NULL\
                              )" 
    cursor.execute(sql)
    connection.commit()