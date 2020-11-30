
class ControllerProducto:
    def addProducto(self, id, nombre, descripcion, stock, nombreProveedor):
        query = 'INSERT INTO stock VALUES(null,' + stock + ')'
        #Ejecute query
        query = 'INSERT INTO producto VALUES(' + id + "\', \'" + nombre + "\', \'" + descripcion + "\', (SELECT idstock FROM stock order by idstock DESC LIMIT 1)" + ", (SELECT idproveedor from proveedor WHERE nombre= \'" + nombreProveedor + "\'))"

        
    def eliminarPruducto(self, id):
        query = 'DELETE FROM producto WHERE idproducto=' + id

    def modificarProducto(self, id, stock):

        query = "UPDATE stock SET stock=" + stock + "WHERE idstock=" + stock
    
