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

    def modificarProveedor(self, id, telefono):

        conn = DatabaseConnection('localhost', 'root', 'qweqwe1', 'final')

        try:
            with conn.connection.cursor() as cursor:
                
                query = "UPDATE proveedor SET telefono=%s  WHERE idproveedor=%s;"
                cursor.execute(query, (telefono, id))   
            conn.connection.commit()    

        finally:
            conn.connection.close()


             