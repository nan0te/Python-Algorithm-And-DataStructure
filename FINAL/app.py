from ViewAddProducto import ViewAddProducto
from controllers.ControllerProveedor import ControllerProveedor

nuevo_proveedor = ControllerProveedor()
nuevo_proveedor.addProveedor('posadas 3213', '223123321', 'LaChola')
nuevo_proveedor.eliminarProveedor('3')
nuevo_proveedor.modificarProveedor('5','223000000')



app = ViewAddProducto()
app.initComponents()
app.crearBotones()







