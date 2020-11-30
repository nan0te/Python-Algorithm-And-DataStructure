from tkinter import *
from Window import Window


class ViewAddProducto:
    def __init__(self):
        self.root = Tk()
        app = Window(self.root)
        self.root.wm_title("FINAL PROGRAMACION II - ISET DIC 2020")
        self.root.geometry("480x480")
        self.root.configure(bg='black')


    def initComponents(self):
        global txtNombreArticulo 
        txtNombreArticulo = Entry(self.root)
        txtNombreArticulo.grid(row = 2, column = 10, padx = 10, pady = 10)
        global txtdesArticulo 
        txtdesArticulo = Entry(self.root)
        txtdesArticulo.grid(row = 3, column = 10, padx = 10, pady = 10)
        global txtStock 
        txtStock = Entry(self.root)
        txtStock.grid( row=4, column = 10, padx = 10, pady = 10)
        global txtNombreProveedor
        txtNombreProveedor = Entry(self.root)
        txtNombreProveedor.grid(row=5, column = 10, padx = 10, pady = 10)

        lblNombreArticulo = Label(self.root, text=' Nombre : ')
        lblNombreArticulo.grid ( row = 2, column = 9, sticky ="e", padx = 10, pady = 10)
        lblDes = Label(self.root, text=' Descripcion : ')
        lblDes.grid ( row = 3, column = 9, sticky ="e", padx = 10, pady = 10)
        lblStock = Label(self.root, text=' Stock : ')
        lblStock.grid ( row = 4, column = 9, sticky ="e", padx = 10, pady = 10)
        lblProveedor = Label(self.root, text=' Proveedor : ')
        lblProveedor.grid ( row = 5, column = 9, sticky ="e", padx = 10, pady = 10)

    
    def addArticulo(self):
        Nombre_articulo = txtNombreArticulo.get()
        Descripcion_articulo = txtdesArticulo.get()
        Stock = txtStock.get()
        NombreProveedor = txtNombreProveedor.get()

        print(Nombre_articulo, Descripcion_articulo, Stock, NombreProveedor )

    def crearBotones(self):
        btn = Button(self.root, text='Guardar', command = self.addArticulo)
        btn.grid(row = 6, column = 10, padx = 15, pady = 15)

        btn = Button(self.root, text='Cancelar')
        btn.grid(row = 6, column = 9, padx = 10, pady = 10)

        self.root.mainloop()