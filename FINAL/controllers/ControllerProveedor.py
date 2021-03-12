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
                
                query = "UPDATE proveedor SET direccion=%s, telefono=%s, nombre=%s WHERE idproveedor=%s;"
                cursor.execute(query, (direccion, telefono, nombreproveedor, id))   
            conn.connection.commit()    

        finally:
            conn.connection.close()

    def obtenerProveedor(self, id):
        conn = DatabaseConnection('localhost', 'root', 'qweqwe1', 'final')
        try:
            with conn.connection.cursor() as cursor:           
                sql = "SELECT telefono, nombre, direccion FROM proveedor where idproveedor=%s;"
                cursor.execute(sql, (id))
                result = cursor.fetchone()           
        finally:
            conn.connection.close()

        return result

    def cb_proveedores(self):
        conn = DatabaseConnection('localhost', 'root', 'qweqwe1', 'final')
        try:
            with conn.connection.cursor() as cursor:           
                sql = "SELECT nombre FROM proveedor;"
                cursor.execute(sql)
                result = cursor.fetchall()      
               
        finally:
            conn.connection.close()

        return result

             