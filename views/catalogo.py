# Imports
from tkinter import *
from modules.load_objects.buttons import load_button
from modules.load_objects.images import load_image

# ------------------------------------------


class catalogo(Frame):
    def __init__(self, master=None):
        super().__init__(master, height=600, width=800, bg="pink")
        self.master = master
        self.pack()
        self.create_widgets

    def create_widgets(self):
        # Imagenes
        self.load_image("./assets/images/argentina1985.png", self, 50, 10)
        self.load_image("./assets/images/avatar.png", self, 50, 360)
        self.load_image("./assets/images/lahuerfana.png", self, 320, 10)
        self.load_image("./assets/images/dontworrydarling.png", self, 590, 10)
        self.load_image("./assets/images/sonrie.png", self, 850, 10)
        self.load_image("./assets/images/blackadamn.png", self, 1100, 10)
        self.load_image("./assets/images/thor.png", self, 320, 360)
        self.load_image("./assets/images/losminions.png", self, 590, 360)
        self.load_image("./assets/images/topgun.png", self, 850, 360)
        self.load_image("./assets/images/blackpanter2.png", self, 1100, 360)

        # ------------------------------------------

        # Botones
        self.load_button(self, "ARGENTINA 1985", 50, 280)
        self.load_button(self, "AVATAR 2", 50, 630)
        self.load_button(self, "DON'T WORRY DARLING", 590, 280)
        self.load_button(self, "LA HUERFANA: EL ORIGEN", 320, 280)
        self.load_button(self, "SONRIE", 850, 280)
        self.load_button(self, "BLACK ADAM", 1100, 280)
        self.load_button(self, "THOR: AMOR Y TRUENO", 320, 630)
        self.load_button(self, "MINIONS: NACE UN VILLANO", 590, 630)
        self.load_button(self, "TOP GUN: MAVERICK", 850, 630)
        self.load_button(self, "BLACK PANTHER 2: WAKANDA FOREVER", 1100, 630)

        # ------------------------------------------
