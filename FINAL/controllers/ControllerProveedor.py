from classes.DatabaseConnection import DatabaseConnection

class ControllerProveedor:
    def addProveedor(self, direccion, telefono, nombre):

        conn = DatabaseConnection('localhost', 'root', 'qweqwe1', 'final')

        try:
            with conn.connection.cursor() as cursor:
                
                sql = "INSERT INTO proveedor VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (0, direccion, telefono, nombre))
           
            conn.connection.commit()

        finally:
            conn.connection.close()


    def eliminarProveedor(self, id):

        conn = DatabaseConnection('localhost', 'root', 'qweqwe1', 'final')

        try:
            with conn.connection.cursor() as cursor:
                
                query = "DELETE FROM proveedor WHERE idproveedor=%s "
                cursor.execute(query, (id))   
            conn.connection.commit()    

        finally:
            conn.connection.close()

    def modificarProveedor(self, id, direccion, telefono, nombreproveedor):

        conn = DatabaseConnection('localhost', 'root', 'qweqwe1', 'final')

        try:
            with conn.connection.cursor() as cursor:
                
                query = "UPDATE proveedor SET direccion=%s, telefono=%s, nombre_proveedor=%s WHERE idproveedor=(SELECT proveedor_idproveedor from producto WHERE idproducto=%s);"
                cursor.execute(query, (direccion, telefono, nombreproveedor, id))   
            conn.connection.commit()    

        finally:
            conn.connection.close()


             