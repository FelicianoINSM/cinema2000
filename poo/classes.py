from tkinter import messagebox

# Class movie

class movie:
    def __init__(self, titulo, sinapsis, genero, duracion, director):
        self.t = titulo
        self.s = sinapsis
        self.g = genero
        self.d = duracion
        self.di = director

    def info(self):
        messagebox.showinfo(title=self.t,
        message=(   ' SINAPSIS: ', self.s,
                    ' GENERO: ', self.g,                                                                
                    ' DURACION: ', self.d,                                                               
                    ' DIRECTOR: ', self.di))

#------------------------------------------