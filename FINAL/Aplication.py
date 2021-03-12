from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Window import Window
from classes.Articulo import Articulo
from classes.Stock import Stock
from classes.Proveedor import Proveedor
from classes.Cliente import Cliente
from controllers.ControllerArticulo import ControllerArticulo
from controllers.ControllerStock import ControllerStock
from controllers.ControllerProveedor import ControllerProveedor
from controllers.ControllerCliente import ControllerCliente
from controllers.ControllerFactura import ControllerFactura

class Aplication:
    def __init__(self):

        self.root = Tk()
        app = Window(self.root)
        self.root.wm_title("FINAL PROGRAMACION II - ISET DIC 2020")
        self.root.geometry("480x480")
        self.root.configure(bg='black')
        self.count = 0

    def salirAplicacion(self):

        resp = messagebox.askquestion("Salir", "Desea salir de la aplicacion?")
        if resp == "yes":
            self.root.destroy()
    
    def limpiarEntrys(self):

        resp = messagebox.askquestion("Limpiar entrys", "Desea limpiar los textos?")
        if resp == "yes":

            entryNombreCliente.set('')   
            entryDireccionCliente.set('')
            entryTelCliente.set('')
            entryDNI.set('') 
            entryNumFactura.set('- - -')
            entryProductoFactura.set('')
            entryCantidadFactura.set('')
            entryImporteFactura.set('- - -')

    def view_add_proveedor(self):

        global entry_id_proveedor
        global txtid_proveedor
        global entryNombreProveedor 
        global txtNombreProveedor
        global entryDireccion
        global txtDireccion
        global entryTelefono
        global txtTelefono
        global lblidproveedor
        global lblProveedor
        global lblDireccion
        global lblTelefono
        self.new = Toplevel(self.root)  
        
        self.new.geometry("400x400+200+200")
        self.new.configure(bg='black')
        
        entry_id_proveedor = StringVar()
        
        txtid_proveedor = Entry(self.new, font=("Segoe UI", 16 ), width=20, textvariable=entry_id_proveedor)
        txtid_proveedor.grid( row=4, column = 10, padx = 10, pady = 10)

        entryNombreProveedor = StringVar()
        
        txtNombreProveedor = Entry(self.new, font=("Segoe UI", 16 ), width=20, textvariable=entryNombreProveedor)
        txtNombreProveedor.grid( row=5, column = 10, padx = 10, pady = 10)

         
        entryDireccion = StringVar()
        
        txtDireccion = Entry(self.new, font=("Segoe UI", 16 ), width=20, textvariable=entryDireccion)
        txtDireccion.grid( row=6, column = 10, padx = 10, pady = 10)

         
        entryTelefono = StringVar()
        
        txtTelefono = Entry(self.new, font=("Segoe UI", 16 ), width=20, textvariable=entryTelefono)
        txtTelefono.grid(  row=7, column = 10, padx = 10, pady = 10)

        lblidproveedor = Label(self.new, text=' ID : ', font=("Segoe UI", 16 ), width=20)
        lblidproveedor.grid (  row = 4, column = 9, sticky ="e", padx = 10, pady = 10)
        lblProveedor = Label(self.new, text=' Proveedor : ', font=("Segoe UI", 16 ), width=20)
        lblProveedor.grid (  row = 5, column = 9, sticky ="e", padx = 10, pady = 10)
        lblDireccion = Label(self.new, text=' Dirrecion : ', font=("Segoe UI", 16 ), width=20)
        lblDireccion.grid (  row = 6, column = 9, sticky ="e", padx = 10, pady = 10)
        lblTelefono = Label(self.new    , text=' Telefono : ', font=("Segoe UI", 16 ), width=20)
        lblTelefono.grid (  row = 7, column = 9, sticky ="e", padx = 10, pady = 10)

        btn = Button(self.new, text='Alta', font=("Segoe UI", 16 ), width=10, command=self.add_proveedor)
        btn.grid(row = 8, column = 9, padx = 10, pady = 10)

        btn = Button(self.new, text='Baja', font=("Segoe UI", 16 ), width=10, command=self.delete_proveedor)
        btn.grid(row = 8, column = 10, padx = 10, pady = 10)

        btn = Button(self.new, text='Modificar', font=("Segoe UI", 16 ), width=10, command= self.edit_proveedor)
        btn.grid(row = 8, column = 11, padx = 10, pady = 10)

        btn = Button(self.new, text='Selecionar', font=("Segoe UI", 16 ), width=10, command=self.get_proveedor)
        btn.grid(row = 8, column = 12, padx = 10, pady = 10)

    def view_add_articulo(self):

        global entry_id_producto
        global txtid_producto
        global entryNombreProducto 
        global txtNombreProducto
        global entryDescripcion
        global txtDescripcion
        global entryCantidad
        global txtCantidad
        global entryIdProveedor
        global txtid_proveedor
        global entryCantidad
        global txtCantidad
        global entryPrecio
        global txtPrecio
        global lblidproducto
        global lblNombreProducto
        global lblDescripcion
        global lblCantidad
        global lblProveedor
        global lblPrecio

        self.new = Toplevel(self.root)  
        
        self.new.geometry("400x400+200+200")
        self.new.configure(bg='black')


        entry_id_producto = StringVar()  
        txtid_producto = Entry(self.new, font=("Segoe UI", 16 ), width=20, textvariable=entry_id_producto)
        txtid_producto.grid( row=4, column = 10, padx = 10, pady = 10)

        entryNombreProducto = StringVar()    
        txtNombreProducto = Entry(self.new, font=("Segoe UI", 16 ), width=20, textvariable=entryNombreProducto)
        txtNombreProducto.grid( row=5, column = 10, padx = 10, pady = 10)
       
        entryDescripcion = StringVar()  
        txtDescripcion = Entry(self.new, font=("Segoe UI", 16 ), width=20, textvariable=entryDescripcion)
        txtDescripcion.grid( row=6, column = 10, padx = 10, pady = 10)

        entryCantidad = StringVar()  
        txtCantidad = Entry(self.new, font=("Segoe UI", 16 ), width=20, textvariable=entryCantidad)
        txtCantidad.grid( row=7, column = 10, padx = 10, pady = 10)

        p = ControllerProveedor() 
        
        result = {}
        result = p.cb_proveedores()
        values = []

        for val in result:
            values.append(val['nombre'])
       
        selected_proveedor = StringVar()

        global proveedor_cb
        proveedor_cb = ttk.Combobox(self.new, textvariable=selected_proveedor, width=20, font=("Segoe UI", 16) )
        proveedor_cb['values'] =  values
        proveedor_cb['state'] = 'readonly'  # normal
        proveedor_cb.grid(column=10, row=8, padx = 10, pady = 10)

        entryPrecio = StringVar()  
        txtPrecio = Entry(self.new, font=("Segoe UI", 16 ), width=20, textvariable=entryPrecio)
        txtPrecio.grid( row=9, column = 10, padx = 10, pady = 10)

        lblidproducto = Label(self.new, text=' ID : ', font=("Segoe UI", 14 ), width=20)
        lblidproducto.grid (  row = 4, column = 9, sticky ="e", padx = 10, pady = 10)
        lblNombreProducto = Label(self.new, text=' Nombre : ', font=("Segoe UI", 14 ), width=20)
        lblNombreProducto.grid (  row = 5, column = 9, sticky ="e", padx = 10, pady = 10)
        lblDescripcion = Label(self.new, text=' Descripcion : ', font=("Segoe UI", 14 ), width=20)
        lblDescripcion.grid (  row = 6, column = 9, sticky ="e", padx = 10, pady = 10)
        lblCantidad = Label(self.new    , text=' Stock : ', font=("Segoe UI", 14 ), width=20)
        lblCantidad.grid (  row = 7, column = 9, sticky ="e", padx = 10, pady = 10)
        lblProveedor = Label(self.new, text=' Proveedor : ', font=("Segoe UI", 14 ), width=20)
        lblProveedor.grid (  row = 8, column = 9, sticky ="e", padx = 10, pady = 10)
        lblPrecio = Label(self.new    , text=' Precio : ', font=("Segoe UI", 14 ), width=20)
        lblPrecio.grid (  row = 9, column = 9, sticky ="e", padx = 10, pady = 10)

        btn = Button(self.new, text='Alta', font=("Segoe UI", 14 ), width=10, command=self.add_articulo)
        btn.grid(row = 11, column = 9, padx = 10, pady = 10)

        btn = Button(self.new, text='Baja', font=("Segoe UI", 14 ), width=10, command=self.delete_articulo)
        btn.grid(row = 11, column = 10, padx = 10, pady = 10)

        btn = Button(self.new, text='Modificar', font=("Segoe UI", 14 ), width=10, command= self.edit_articulo)
        btn.grid(row = 11, column = 11, padx = 10, pady = 10)

        btn = Button(self.new, text='Selecionar', font=("Segoe UI", 14 ), width=10, command=self.get_articulo)
        btn.grid(row = 11, column = 12, padx = 10, pady = 10)


    def initComponents(self):

        menu = Menu(self.root)
        self.root.config(menu=menu)

        mnuArchivo = Menu(menu)
        mnuArchivo.add_command(label="Proveedores",  command= self.view_add_proveedor)
        mnuArchivo.add_command(label="Articulos",  command= self.view_add_articulo)
        mnuArchivo.add_command(label="Vaciar Entrys", command= self.limpiarEntrys)
        mnuArchivo.add_separator()
        mnuArchivo.add_command(label="Exit", command=self.salirAplicacion)
        menu.add_cascade(label="Archivo", menu=mnuArchivo)

        global lblNombreCliente
        global lblDireccionCliente
        global lblTelCliente
        global lblDNI
        global lblNumeroFactura
        global lbltxtNumFactura
        global entryNombreCliente
        global entryTelCliente
        global entryDireccionCliente
        global entryDNI
        global lblConceptos
        global lblProductoFactura
        global entryCantidadFactura
        global entryIdProveedor
        global entryProductoFactura
        global entryidfactura
        global entryIdDetalleFactura
        global entryImporteFactura

        entryidfactura = StringVar()
        global txtIDClienteFactura
        txtIDClienteFactura = Entry(self.root, font=("Segoe UI", 12 ), width=20, textvariable=entryidfactura )
        txtIDClienteFactura.grid(  row = 2, column = 10, padx = 10, pady = 10)

        entryNombreCliente = StringVar()
        global txtNombreCliente
        txtNombreCliente = Entry(self.root, font=("Segoe UI", 12 ), width=20, textvariable=entryNombreCliente )
        txtNombreCliente.grid(  row = 3, column = 10, padx = 10, pady = 10)
 
        entryTelCliente = StringVar()
        global txtTelCliente 
        txtTelCliente = Entry(self.root, font=("Segoe UI", 12 ), width=20, textvariable=entryTelCliente)
        txtTelCliente.grid( row = 4, column = 10, padx = 10, pady = 10)
     
        entryDireccionCliente = StringVar()
        global txtDireccionCliente 
        txtDireccionCliente = Entry(self.root, font=("Segoe UI", 12 ), width=20, textvariable=entryDireccionCliente)
        txtDireccionCliente.grid( row = 5, column = 10, padx = 10, pady = 10)

        entryDNI = StringVar()
        global txtDNI 
        txtDNI = Entry(self.root, font=("Segoe UI", 12 ), width=20, textvariable=entryDNI)
        txtDNI.grid( row = 6, column = 10, padx = 10, pady = 10)

        entryIdDetalleFactura = StringVar()
        global txtIdDetalleFactura 
        txtIdDetalleFactura = Entry(self.root, font=("Segoe UI", 12 ), width=20, textvariable=entryIdDetalleFactura)
        txtIdDetalleFactura.grid( row = 9, column = 10, padx = 10, pady = 10)
        entryIdDetalleFactura.set('- - -')

        entryProductoFactura = StringVar()
        global txtProductoFactura 
        txtProductoFactura = Entry(self.root, font=("Segoe UI", 12 ), width=20, textvariable=entryProductoFactura)
        txtProductoFactura.grid( row = 10, column = 10, padx = 10, pady = 10)    
      
        entryCantidadFactura = StringVar()
        global txtCantidadFactura 
        txtCantidadFactura = Entry(self.root, font=("Segoe UI", 12 ), width=20, textvariable=entryCantidadFactura)
        txtCantidadFactura.grid( row = 11, column = 10, padx = 10, pady = 10) 


        entryImporteFactura = StringVar()
        global txtImporteFactura 
        txtImporteFactura = Entry(self.root, font=("Segoe UI", 12 ), width=20, textvariable=entryImporteFactura)
        txtImporteFactura.grid( row = 12, column = 10, padx = 10, pady = 10) 
        entryImporteFactura.set('- - - -')


        lblDatosComprador = Label(self.root, text=' Datos comprador ', font=("Segoe UI", 12), width=20)
        lblDatosComprador.grid (  row = 1, column = 9, sticky ="e", padx = 10, pady = 10)
        lblidClienteFactura = Label(self.root, text=' id: ', font=("Segoe UI", 12 ), width=20)
        lblidClienteFactura.grid (  row = 2, column = 9, sticky ="e", padx = 10, pady = 12)
        lblNombreCliente = Label(self.root, text=' nombre: ', font=("Segoe UI", 12 ), width=20)
        lblNombreCliente.grid (  row = 3, column = 9, sticky ="e", padx = 10, pady = 12)
        lblTelCliente = Label(self.root, text=' telefono/celular: ', font=("Segoe UI", 12 ), width=20)
        lblTelCliente.grid (  row = 4, column = 9, sticky ="e", padx = 10, pady = 10)
        lblDireccionCliente = Label(self.root, text=' dirreccion: ', font=("Segoe UI", 12 ), width=20)
        lblDireccionCliente.grid (  row = 5, column = 9, sticky ="e", padx = 10, pady = 10)
        lblDNI = Label(self.root, text=' dni: ', font=("Segoe UI", 12 ), width=20)
        lblDNI.grid (  row = 6, column = 9, sticky ="e", padx = 10, pady = 10)
        lblNumeroFactura = Label(self.root, text=' numero de factura: ', font=("Segoe UI", 12 ), width=20)
        lblNumeroFactura.grid (  row = 7, column = 9, sticky ="e", padx = 10, pady = 10)
        global entryNumFactura 
        entryNumFactura = StringVar()
        txtNumFactura = Entry(self.root,  font=("Segoe UI", 12 ), width=20, textvariable=entryNumFactura)
        txtNumFactura.grid (  row = 7, column = 10, sticky ="e", padx = 10, pady = 10)
        entryNumFactura.set('-----')
        lblConceptos = Label(self.root, text='Conceptos ', font=("Segoe UI", 12), width=20)
        lblConceptos.grid (  row = 8, column = 9, sticky ="e", padx = 10, pady = 10)
        lblIdDetalleFactura = Label(self.root, text='id: ', font=("Segoe UI", 12 ), width=20)
        lblIdDetalleFactura.grid (  row = 9, column = 9, sticky ="e", padx = 10, pady = 10)
        lblProductoFactura = Label(self.root, text='articulo: ', font=("Segoe UI", 12 ), width=20)
        lblProductoFactura.grid (  row = 10, column = 9, sticky ="e", padx = 10, pady = 10)
        lblCantidadPFactura = Label(self.root, text='cantidad: ', font=("Segoe UI", 12 ), width=20)
        lblCantidadPFactura.grid (  row = 11, column = 9, sticky ="e", padx = 10, pady = 10)
        lblImporteFactura = Label(self.root, text='importe: ', font=("Segoe UI", 12 ), width=20)
        lblImporteFactura.grid (  row = 12, column = 9, sticky ="e", padx = 10, pady = 10)
     

#factira ###############################################################################
    def add_factura(self):
    
        global cliente

        resp = messagebox.askquestion("Agregar", "Esta seguro que desea agregar este producto?")
        if resp == "yes":
            cliente = Cliente(txtNombreCliente.get(), txtTelCliente.get(), txtDireccionCliente.get(), txtDNI.get() )
            controller_cliente = ControllerCliente()
            controller_cliente.add_cliente(cliente.getNombre(), cliente.getTel(), cliente.getDireccion(), cliente.getDNI())
            controller_factura = ControllerFactura()
            num_factura = controller_factura.getNumFactura()
            print(num_factura)
            controller_factura.add(num_factura, txtDNI.get())

            
            messagebox.showinfo(title=None, message='Cliente agregado correctamente')

    def get_factura(self):

        idfactura = ControllerFactura()
        result = idfactura.obtener_factura(txtIDClienteFactura.get())

        if  not (result['nombre_cliente']):
            messagebox.showerror("Error", "Factura inexistente!")        
        
        else:
            entryNombreCliente.set(result['nombre_cliente'])   
            entryDireccionCliente.set(result['direccion_cliente'])
            entryTelCliente.set(result['telefono_cliente'])
            entryDNI.set(result['DNI'])
            entryNumFactura.set('N0000' + result['numero'])
            entryProductoFactura.set(result['producto_idproducto'])
            entryCantidadFactura.set(result['cantidad'])
            entryImporteFactura.set(result['importe'])
    
    def edit_factura(self):
        resp = messagebox.askquestion("Modificar", "Esta seguro que desea modificar esta factura?")
     
        if resp == "yes": 
            factura_modificada = ControllerFactura()
            factura_modificada.modificar_factura(txtIDClienteFactura.get(), txtNombreCliente.get(), txtTelCliente.get(), txtDireccionCliente.get(), txtDNI.get(), txtProductoFactura.get(), txtCantidadFactura.get() )
            messagebox.showinfo(title=None, message='Producto modificado correctamente')
            entryNombreCliente.set('')   
            entryDireccionCliente.set('')
            entryTelCliente.set('')
            entryDNI.set('') 
            entryNumFactura.set('---')
            entryProductoFactura.set('')
            entryCantidadFactura.set('')
            entryImporteFactura.set('- - -')

    def delete_factura(self):
        resp = messagebox.askquestion("Eliminar", "Esta seguro que desea eliminar este producto?")
        if resp == "yes":  
            proveedor = ControllerFactura()
            proveedor.eliminar_factura(txtIDClienteFactura.get())
            messagebox.showinfo(title=None, message='Producto eliminaddo correctamente')
            entryNombreCliente.set('')   
            entryDireccionCliente.set('')
            entryTelCliente.set('')
            entryDNI.set('') 
            entryNumFactura.set('---')
            entryProductoFactura.set('')
            entryCantidadFactura.set('')
            entryImporteFactura.set('- - -')





#proveedor ###########################################################################

    def add_proveedor(self):

        global proveedor
        proveedor = Proveedor(txtDireccion.get(), txtTelefono.get(), txtNombreProveedor.get())
       
        resp = messagebox.askquestion("Agregar", "Esta seguro que desea agregar este producto?")
        if resp == "yes":
            nuevo_proveedor = ControllerProveedor()
            nuevo_proveedor.addProveedor(proveedor.getDireccion(), proveedor.getTelefono(), proveedor.getNombre())
            
    def delete_proveedor(self):
        resp = messagebox.askquestion("Eliminar", "Esta seguro que desea eliminar este producto?")
        if resp == "yes":  
            proveedor = ControllerProveedor()
            proveedor.eliminarProveedor(txtid_proveedor.get())
            res = messagebox.askquestion("", "producto eliminado")
            if resp == "yes": 
                entry_id_proveedor.set('')
                entryDireccion.set('')
                entryNombreProveedor.set('')
                entryTelefono.set('')

    def get_proveedor(self):
        proveedor = ControllerProveedor() 
        result = proveedor.obtenerProveedor(txtid_proveedor.get())
    
        if  not (result['nombre']):
            messagebox.showerror("Error", "Proveedor inexistente!")        
        
        else:
            entryNombreProveedor.set(result['nombre'])   
            entryDireccion.set(result['direccion'])
            entryTelefono.set(result['telefono'])

    def edit_proveedor(self):

        resp = messagebox.askquestion("Modificar", "Esta seguro que desea modificar este producto?")
     
        if resp == "yes": 
            proveedor = Proveedor(txtDireccion.get(), txtTelefono.get(), txtNombreProveedor.get())
            proveedor_modificado = ControllerProveedor() 
            proveedor_modificado.modificarProveedor(txtid_proveedor.get(), proveedor.getDireccion(), proveedor.getTelefono(), proveedor.getNombre())
            entry_id_proveedor.set('')
            entryDireccion.set('')
            entryTelefono.set('')
            messagebox.showinfo(title=None, message='Producto modificado correctamente')


# articulo ################################################################################

    def add_articulo(self):

        producto = Articulo(txtNombreProducto.get(), txtDescripcion.get(), txtCantidad.get(), proveedor_cb.get(), txtPrecio.get() )

        resp = messagebox.askquestion("Agregar", "Esta seguro que desea agregar este producto?")
        if resp == "yes":
            nuevo_articulo = ControllerArticulo()
            nuevo_articulo.add_producto(producto.getNombre(), producto.getDescripcion(), producto.getStock(), producto.getNombreProveedor(), producto.getPrecio())
            messagebox.showinfo(title=None, message='Producto agregado correctamente')

    def add_item_factura(self):

        itemnuevo = ControllerFactura()
        itemnuevo.add_producto_factura(txtCantidadFactura.get(), txtProductoFactura.get())
        messagebox.showinfo(title=None, message='Item agregado correctamente')



    def get_articulo(self):

        getProducto = ControllerArticulo() 
        result = getProducto.obtenerProducto(txtid_producto.get())
 
        entryNombreProducto.set(result['nombre'])
        entryDescripcion.set(result['descripcion'])
        entryCantidad.set(result['cantidad'])
        proveedor_cb.set(result['proveedor'])
        entryPrecio.set(result['precio'])
          
    def delete_articulo(self):

        resp = messagebox.askquestion("Eliminar", "Esta seguro que desea eliminar este producto?")
        if resp == "yes":  
            producto = ControllerArticulo()
            producto.eliminarProducto(txtid_producto.get())
            messagebox.showinfo(title=None, message='Producto eliminado correctamente') 
            entry_id_producto.set('')
            entryNombreProducto.set('')
            entryDescripcion.set('')
            entryCantidad.set('')
            proveedor_cb.set('')
            entryPrecio.set('')

    def edit_articulo(self):

        resp = messagebox.askquestion("Modificar", "Esta seguro que desea modificar este producto?")
        
        if resp == "yes": 

            editarProducto = ControllerArticulo()
            editarProducto.modificarProducto(txtid_producto.get(), txtNombreProducto.get(), txtDescripcion.get(), txtCantidad.get(), txtPrecio.get() )

            messagebox.showinfo(title=None, message='Producto modificado correctamente')      
            entry_id_producto.set('')
            entryNombreProducto.set('')
            entryDescripcion.set('')
            entryCantidad.set('')
            proveedor_cb.set('')
            entryPrecio.set('')                

    def crearBotones(self):
        btn = Button(self.root, text='Alta', font=("Segoe UI", 16 ), width=10, command=self.add_factura)
        btn.grid(row = 13, column = 9, padx = 10, pady = 10)

        btn = Button(self.root, text='Baja', font=("Segoe UI", 16 ), width=10, command=self.delete_factura)
        btn.grid(row = 13, column = 10, padx = 10, pady = 10)

        btn = Button(self.root, text='Modificar', font=("Segoe UI", 16 ), width=10, command=self.edit_factura )
        btn.grid(row = 13, column = 11, padx = 10, pady = 10)

        btn = Button(self.root, text='Selecionar', font=("Segoe UI", 16 ), width=10, command=self.get_factura)
        btn.grid(row = 13, column = 12, padx = 10, pady = 10)

        btn = Button(self.root, text='cargar', font=("Segoe UI", 10 ), width=8, command = self.add_item_factura)
        btn.grid(row = 11, column = 11, padx = 3, pady = 3)

        btn = Button(self.root, text='Modificar', font=("Segoe UI", 10 ), width=8, command = self.add_item_factura)
        btn.grid(row = 11, column = 12, padx = 3, pady = 3)

        btn = Button(self.root, text='eliminar', font=("Segoe UI", 10 ), width=8, command = self.add_item_factura)
        btn.grid(row = 11, column = 13, padx = 3, pady = 3)

        self.root.mainloop()