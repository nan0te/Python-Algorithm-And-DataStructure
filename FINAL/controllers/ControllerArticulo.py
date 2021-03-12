from classes.DatabaseConnection import DatabaseConnection

class ControllerArticulo:
    def add_producto(self,  nombre, descripcion, cantidad, proveedor, precio):
        conn = DatabaseConnection('localhost', 'root', 'qweqwe1', 'final')
        try:
            with conn.connection.cursor() as cursor:                
                sql = "INSERT INTO producto VALUES (%s, %s, %s, %s, (SELECT idproveedor from proveedor WHERE nombre=%s), %s )"
                cursor.execute(sql, (0, nombre, descripcion, cantidad, proveedor, precio))
           
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
        
    def modificarProducto(self, id, nombre, descripcion, stock, precio):
      
        conn = DatabaseConnection('localhost', 'root', 'qweqwe1', 'final')
        try:
            with conn.connection.cursor() as cursor:              
                sql = "UPDATE producto SET nombre=%s, descripcion=%s, cantidad=%s, precio=%s WHERE idproducto=%s;"
               
                cursor.execute(sql, (nombre, descripcion, stock, precio, id))
        
            conn.connection.commit()

        finally:
            conn.connection.close()

    def obtenerProducto(self, id):

        conn = DatabaseConnection('localhost', 'root', 'qweqwe1', 'final')
        try:
            with conn.connection.cursor() as cursor:           
                sql = "SELECT pr.nombre AS proveedor, p.nombre, p.descripcion, p.cantidad, p.precio from producto p INNER JOIN proveedor pr where idproducto=%s;"
                cursor.execute(sql, (id))
                result = cursor.fetchone()           
        finally:
            conn.connection.close()

        return result


    
 