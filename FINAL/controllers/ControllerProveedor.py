
class ControllerProveedor:
    def addProveedor(self, id, direccion, telefono, nombre):

        query = "INSERT INTO proveedor VALUES(" + id + ",\'" + direccion + "\', \'" + telefono + "\', \'" + nombre + "\')"

    def eliminarProveedor(self, id):

        query = "DELETE FROM proveedor WHERE idproveedor= " + id

    def modificarProveedor(self, id, telefono):

        query = "UPDATE proveedor SET  telefono=\'" + telefono + "\' WHERE idproveedor= " + id

             