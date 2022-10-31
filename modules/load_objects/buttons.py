from tkinter import Button
import modules.db.get


def load_button(frame, movie, xcoor, ycoor):
    btn = Button(
        frame,
        font=("Calibri", 12, "bold"),
        text="▶",
        command=lambda: modules.db.get.data_get(movie),
    )
    btn.pack(x=xcoor, y=ycoor)
