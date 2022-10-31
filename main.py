from tkinter import *
import modules.db.tables
import modules.local_req
import views.catalogo

modules.db.tables.tablaPeliculas()
modules.local_req.hardcode_upload()

root = Tk()
# root.rowconfigure(0, weight=1)
# root.columnconfigure(0, weight=1)
# root.state("zoomed")
# root.title("Cinema2000")

root.wm_title("Cinema 2000")
app = views.catalogo.catalogo(root)
app.mainloop()
