from classes.DatabaseConnection import DatabaseConnection

class ControllerStock:
    def addStock(self, stock):
        conn = DatabaseConnection('localhost', 'root', 'qweqwe1', 'final')
        try:
            with conn.connection.cursor() as cursor:              
                query = "INSERT INTO stock VALUES (%s, %s)"
                cursor.execute(query, (0, stock))         
            conn.connection.commit()
        finally:
            conn.connection.close()

    def modificarStock(self, id, stock):
        conn = DatabaseConnection('localhost', 'root', 'qweqwe1', 'final')
        try:
            with conn.connection.cursor() as cursor:             
                query = "UPDATE stock SET cantidad=%s WHERE idstock=(SELECT stock_idstock from producto WHERE idproducto=%s);"
                cursor.execute(query, (stock, id))   
            conn.connection.commit()    
        finally:
            conn.connection.close()