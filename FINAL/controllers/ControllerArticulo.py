from classes.DatabaseConnection import DatabaseConnection

class ControllerArticulo:
    def addProducto(self,  nombre, descripcion, nombreProveedor):
        conn = DatabaseConnection('localhost', 'root', 'qweqwe1', 'final')
        try:
            with conn.connection.cursor() as cursor:                
                sql = "INSERT INTO producto VALUES (%s, %s, %s, (SELECT idproveedor from proveedor WHERE nombre_proveedor=%s), (SELECT idstock FROM stock ORDER BY idstock DESC LIMIT 1))"
                cursor.execute(sql, (0, nombre, descripcion, nombreProveedor))
           
            conn.connection.commit()
        finally:
            conn.connection.close()
        
    def eliminarProducto(self, id):
        conn = DatabaseConnection('localhost', 'root', 'qweqwe1', 'final')
        try:
            with conn.connection.cursor() as cursor:                  
                query = "DELETE FROM producto WHERE idproducto=%s;"
                query2 = "DELETE FROM producto WHERE idproducto=%s;"
                cursor.execute(query, (id))
                cursor.execute(query2, (id))
           
            conn.connection.commit()   

        finally:
            conn.connection.close()
        
    def modificarProducto(self, id, nombre, stock, descripcion, nombreproveedor, direccion, telefono):
      
        conn = DatabaseConnection('localhost', 'root', 'qweqwe1', 'final')
        try:
            with conn.connection.cursor() as cursor:              
                sql = "UPDATE producto SET nombre=%s, descripcion=%s WHERE idproducto=%s;"
                #sql2 = "UPDATE stock SET cantidad=%s WHERE idstock=%s;"
                #sql3 = "UPDATE proveedor SET direccion=%s, telefono=%s, nombre_proveedor=%s WHERE idproveedor=(SELECT proveedor_idproeedor from producto WHERE idproducto=%s);"
                cursor.execute(sql, (nombre, descripcion, id))
                #cursor.execute(sql2, (stock, id))
                #cursor.execute(sql3, (direccion, telefono, nombreproveedor, id))
            conn.connection.commit()

        finally:
            conn.connection.close()

    def obtenerProducto(self, id):

        conn = DatabaseConnection('localhost', 'root', 'qweqwe1', 'final')
        try:
            with conn.connection.cursor() as cursor:           
                sql = "SELECT p.*, pr.*, s.cantidad  from producto p JOIN proveedor pr ON p.idproducto=pr.idproveedor JOIN stock s ON p.idproducto=s.idstock WHERE idproducto=%s;"
                cursor.execute(sql, (id))
                result = cursor.fetchone()           
        finally:
            conn.connection.close()

        return result


    
 