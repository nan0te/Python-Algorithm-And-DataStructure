from tkinter import *
from tkinter import ttk

def ViewProveedores():
    
    root = Tk()
    root.wm_title("FINAL PROGRAMACION II - ISET DIC 2020")
    root.geometry("480x480")
    root.configure(bg='white')

    tabla = self.ttk.Treeview(columns=4)
    tabla.pack()
    tabla.grid(height=10,   row=4, column=0,columnspan=2)
    tabla.heading("#0", text="ID", anchor=CENTER)
    tabla.heading("#1", text="Direccion", anchor=CENTER)
    tabla.heading("#2", text="Telefono", anchor=CENTER)
    tabla.heading("#3", text="Nombre", anchor=CENTER)



class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        mnuArchivo = Menu(menu)
        mnuArchivo.add_command(label="Proveedores", command=ViewProveedores)
        mnuArchivo.add_separator()
        mnuArchivo.add_command(label="Exit")
        menu.add_cascade(label="Archivo", menu=mnuArchivo)

        
        



