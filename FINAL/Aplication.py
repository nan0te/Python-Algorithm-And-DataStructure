from tkinter import *
from tkinter import messagebox
from Window import Window
from classes.Articulo import Articulo
from classes.Stock import Stock
from classes.Proveedor import Proveedor
from controllers.ControllerArticulo import ControllerArticulo
from controllers.ControllerStock import ControllerStock
from controllers.ControllerProveedor import ControllerProveedor



class Aplication:
    def __init__(self):

        self.root = Tk()
        app = Window(self.root)
        self.root.wm_title("FINAL PROGRAMACION II - ISET DIC 2020")
        self.root.geometry("480x480")
        self.root.configure(bg='black')

    def salirAplicacion(self):

        resp = messagebox.askquestion("Salir", "Desea salir de la aplicacion?")
        if resp == "yes":
            self.root.destroy()
    
    def limpiarEntrys(self):

        resp = messagebox.askquestion("Limpiar entrys", "Desea limpiar los textos?")
        if resp == "yes":
            entryID.set('')
            entryNombreArticulo.set('')
            entrydesArticulo.set('')
            entryStock.set('')
            entryNombreProveedor.set('')
            entryDireccion.set('')
            entryTelefono.set('')

    def initComponents(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)

        mnuArchivo = Menu(menu)
        mnuArchivo.add_command(label="Proveedores")
        mnuArchivo.add_command(label="Vaciar Entrys", command= self.limpiarEntrys)
        mnuArchivo.add_separator()
        mnuArchivo.add_command(label="Exit", command=self.salirAplicacion)
        menu.add_cascade(label="Archivo", menu=mnuArchivo)

        global entryID 
        entryID = StringVar()
        global txtID
        txtID = Entry(self.root, font=("Segoe UI", 16 ), width=20, textvariable=entryID )
        txtID.grid(  row = 1, column = 10, padx = 10, pady = 10)

        global entryNombreArticulo 
        entryNombreArticulo = StringVar()
        global txtNombreArticulo 
        txtNombreArticulo = Entry(self.root, font=("Segoe UI", 16 ), width=20, textvariable=entryNombreArticulo)
        txtNombreArticulo.grid( row = 2, column = 10, padx = 10, pady = 10)

        global entrydesArticulo 
        entrydesArticulo = StringVar()
        global txtdesArticulo 
        txtdesArticulo = Entry(self.root, font=("Segoe UI", 16 ), width=20, textvariable=entrydesArticulo)
        txtdesArticulo.grid( row = 3, column = 10, padx = 10, pady = 10)

        global entryStock 
        entryStock = StringVar()
        global txtStock 
        txtStock = Entry(self.root, font=("Segoe UI", 16 ), width=20, textvariable=entryStock)
        txtStock.grid(  row=4, column = 10, padx = 10, pady = 10)

        global entryNombreProveedor 
        entryNombreProveedor = StringVar()
        global txtNombreProveedor
        txtNombreProveedor = Entry(self.root, font=("Segoe UI", 16 ), width=20, textvariable=entryNombreProveedor)
        txtNombreProveedor.grid( row=5, column = 10, padx = 10, pady = 10)

        global entryDireccion 
        entryDireccion = StringVar()
        global txtDireccion
        txtDireccion = Entry(self.root, font=("Segoe UI", 16 ), width=20, textvariable=entryDireccion)
        txtDireccion.grid( row=6, column = 10, padx = 10, pady = 10)

        global entryTelefono 
        entryTelefono = StringVar()
        global txtTelefono
        txtTelefono = Entry(self.root, font=("Segoe UI", 16 ), width=20, textvariable=entryTelefono)
        txtTelefono.grid(  row=7, column = 10, padx = 10, pady = 10)
        
        lblID = Label(self.root, text=' ID: ', font=("Segoe UI", 16), width=20)
        lblID.grid (  row = 1, column = 9, sticky ="e", padx = 10, pady = 10)
        lblNombreArticulo = Label(self.root, text=' Nombre : ', font=("Segoe UI", 16 ), width=20)
        lblNombreArticulo.grid (  row = 2, column = 9, sticky ="e", padx = 10, pady = 10)
        lblDes = Label(self.root, text=' Descripcion : ', font=("Segoe UI", 16 ), width=20)
        lblDes.grid (  row = 3, column = 9, sticky ="e", padx = 10, pady = 10)
        lblStock = Label(self.root, text=' Stock : ', font=("Segoe UI", 16 ), width=20)
        lblStock.grid (  row = 4, column = 9, sticky ="e", padx = 10, pady = 10)
        lblProveedor = Label(self.root, text=' Proveedor : ', font=("Segoe UI", 16 ), width=20)
        lblProveedor.grid (  row = 5, column = 9, sticky ="e", padx = 10, pady = 10)
        lblDireccion = Label(self.root, text=' Dirrecion : ', font=("Segoe UI", 16 ), width=20)
        lblDireccion.grid (  row = 6, column = 9, sticky ="e", padx = 10, pady = 10)
        lblTelefono = Label(self.root, text=' Telefono : ', font=("Segoe UI", 16 ), width=20)
        lblTelefono.grid (  row = 7, column = 9, sticky ="e", padx = 10, pady = 10)
   
    def addArticulo(self):

        global stock
        global proveedor
        global producto

        stock = Stock(txtStock.get())   
        proveedor = Proveedor(txtDireccion.get(), txtTelefono.get(),txtNombreProveedor.get())

        Nombre_articulo = txtNombreArticulo.get()
        Descripcion_articulo = txtdesArticulo.get()

        producto = Articulo(Nombre_articulo, Descripcion_articulo, txtStock.get(), txtNombreProveedor.get())

        resp = messagebox.askquestion("Agregar", "Esta seguro que desea agregar este producto?")
        if resp == "yes":
            nuevo_stock = ControllerStock()
            nuevo_stock.addStock(txtStock.get())
            nuevo_proveedor = ControllerProveedor()
            nuevo_proveedor.addProveedor(proveedor.getDireccion(), proveedor.getTelefono(), proveedor.getNombre())
            nuevo_articulo = ControllerArticulo()
            nuevo_articulo.addProducto(producto.getNombre(), producto.getDescripcion(), producto.getNombreProveedor())
        #print(producto.getNombre(), producto.getDescripcion(), producto.getStock(), proveedor.getDireccion(), proveedor.getTelefono(), producto.getNombreProveedor() )
    def getProducto(self):

        getProducto = ControllerArticulo() 
        result = getProducto.obtenerProducto(txtID.get())
        
        entryNombreArticulo.set(result['nombre'])
        entrydesArticulo.set(result['descripcion'])
        entryStock.set(result['cantidad'])
        entryNombreProveedor.set(result['nombre_proveedor'])
        entryDireccion.set(result['direccion'])
        entryTelefono.set(result['telefono'])
          
    def eliminarProducto(self):

        resp = messagebox.askquestion("Eliminar", "Esta seguro que desea eliminar este producto?")
        if resp == "yes":  
            producto = ControllerArticulo()
            producto.eliminarProducto(txtID.get())
            res = messagebox.askquestion("", "producto eliminado")
            if resp == "aceptar": 
                entryID.set('')
                entryNombreArticulo.set('')
                entrydesArticulo.set('')
                entryStock.set('')
                entryNombreProveedor.set('')
                entryDireccion.set('')
                entryTelefono.set('')

    def modificarProducto(self):

        global stock
        global proveedor
        global producto

        stock = Stock(txtStock.get())   
        proveedor = Proveedor(txtDireccion.get(), txtTelefono.get(), txtNombreProveedor.get())

        Nombre_articulo = txtNombreArticulo.get()
        Descripcion_articulo = txtdesArticulo.get()

        producto = Articulo(Nombre_articulo, Descripcion_articulo, txtStock.get(), txtNombreProveedor.get())

        resp = messagebox.askquestion("Modificar", "Esta seguro que desea modificar este producto?")
        
        if resp == "yes": 
            editarProducto = ControllerArticulo()
            editarProducto.modificarProducto(txtID.get(), producto.getNombre(), stock.getStock(), producto.getDescripcion(), proveedor.getNombre(), proveedor.getDireccion(), proveedor.getTelefono() )
            
            editarProvedor = ControllerProveedor()
            editarProvedor.modificarProveedor(txtID.get(), proveedor.getDireccion(), proveedor.getTelefono(), proveedor.getNombre())
            
            editarStock = ControllerStock()
            editarStock.modificarStock(txtID.get(), stock.getStock())
           
            entryID.set('')
            entryNombreArticulo.set('')
            entrydesArticulo.set('')
            entryStock.set('')
            entryNombreProveedor.set('')
            entryDireccion.set('')                
            entryTelefono.set('')

    def crearBotones(self):
        btn = Button(self.root, text='Alta', font=("Segoe UI", 16 ), width=10, command=self.addArticulo)
        btn.grid(row = 8, column = 9, padx = 10, pady = 10)

        btn = Button(self.root, text='Baja', font=("Segoe UI", 16 ), width=10, command=self.eliminarProducto)
        btn.grid(row = 8, column = 10, padx = 10, pady = 10)

        btn = Button(self.root, text='Modificar', font=("Segoe UI", 16 ), width=10, command= self.modificarProducto)
        btn.grid(row = 8, column = 11, padx = 10, pady = 10)

        btn = Button(self.root, text='Selecionar', font=("Segoe UI", 16 ), width=10, command=self.getProducto)
        btn.grid(row = 8, column = 12, padx = 10, pady = 10)

        self.root.mainloop()