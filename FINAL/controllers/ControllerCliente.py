from classes.DatabaseConnection import DatabaseConnection

class ControllerCliente:
    def add_cliente(self, nombre, telefono, direccion, dni):
        conn = DatabaseConnection('localhost', 'root', 'qweqwe1', 'final')

        try:
            with conn.connection.cursor() as cursor:
                
                sql = "INSERT INTO cliente VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (0, nombre, telefono, direccion, dni))
           
            conn.connection.commit()

        finally:
            conn.connection.close()