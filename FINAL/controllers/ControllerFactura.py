from classes.DatabaseConnection import DatabaseConnection
from datetime import datetime

class ControllerFactura:
    def add(self, numero, DNI):
        conn = DatabaseConnection('localhost', 'root', 'qweqwe1', 'final')

        try:
            with conn.connection.cursor() as cursor:
                now = datetime.now()
                formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
                IVA = 21.00
                sql = "INSERT INTO factura VALUES (%s, %s, %s, %s, (select idcliente from cliente where DNI=%s))"
                cursor.execute(sql, (0, numero, formatted_date, IVA, DNI) )
                    
           
            conn.connection.commit()
        
        finally:
            conn.connection.close()

    def add_producto_factura(self, cantidad, producto):
        conn = DatabaseConnection('localhost', 'root', 'qweqwe1', 'final')

        count = int(cantidad)
        try:
            with conn.connection.cursor() as cursor:
                sql2 = "INSERT INTO detalle_factura VALUES (%s, %s, (select precio*%s from producto WHERE idproducto=%s ), %s, (SELECT idfactura from factura ORDER BY idfactura desc limit 1))"
                cursor.execute(sql2, (0, cantidad, count, producto, producto) )
            conn.connection.commit()
        
        finally:
            conn.connection.close()


    def modificar_factura(self, id, nombre, tel, direccion, dni, producto, cantidad):
        conn = DatabaseConnection('localhost', 'root', 'qweqwe1', 'final')
        try:
            with conn.connection.cursor() as cursor:              
                sql = "update  cliente,factura,detalle_factura SET nombre_cliente = %s, telefono_cliente=%s, direccion_cliente=%s, DNI=%s, detalle_factura.producto_idproducto = %s, detalle_factura.cantidad = %s, detalle_factura.importe = (SELECT precio from producto WHERE idproducto = %s)*%s WHERE cliente.idcliente = factura.cliente_idcliente AND factura.idfactura = detalle_factura.factura_idfactura AND detalle_factura.iddetalle = %s;"
               
                cursor.execute(sql, (nombre, tel, direccion, dni, producto, cantidad, producto, cantidad, id))
        
            conn.connection.commit()

        finally:
            conn.connection.close()


    def eliminar_factura(self, id):

        conn = DatabaseConnection('localhost', 'root', 'qweqwe1', 'final')
        try:
            with conn.connection.cursor() as cursor:                  
                query = "SET @idfactura = (SELECT factura_idfactura FROM detalle_factura where iddetalle=%s)"
                cursor.execute(query, (id))
                query1 = "SET @idcliente = (SELECT cliente_idcliente FROM factura where idfactura=@idfactura)"
                cursor.execute(query1)
                query2 = "delete from detalle_factura where factura_idfactura=@idfactura;"
                cursor.execute(query2)
                query4 = "delete from factura WHERE idfactura = @idfactura"
                cursor.execute(query4)    
                query3 = "delete from cliente WHERE idcliente=@idcliente"
                cursor.execute(query3)  
            conn.connection.commit() 

        except:  
            print("Can't delete !")  
            cursor.rollback()    

        finally:
            conn.connection.close()



    def obtener_factura(self, id):
        conn = DatabaseConnection('localhost', 'root', 'qweqwe1', 'final')
        try:
            with conn.connection.cursor() as cursor:           
                sql = "SELECT c.nombre_cliente, c.telefono_cliente, c.direccion_cliente, c.DNI, f.numero, d.producto_idproducto, d.cantidad, d.importe from cliente c JOIN factura f ON c.idcliente = f.cliente_idcliente JOIN detalle_factura d ON f.idfactura = d.factura_idfactura WHERE d.iddetalle =%s"
                cursor.execute(sql, (id))
                result = cursor.fetchone()           
        finally:
            conn.connection.close()

        return result
             

    def getNumFactura(self):
        conn = DatabaseConnection('localhost', 'root', 'qweqwe1', 'final')
        try:
            with conn.connection.cursor() as cursor:           
                sql = "SELECT idcliente from cliente ORDER BY idcliente DESC LIMIT 1"
                cursor.execute(sql)
                result = cursor.fetchone()
                result = result['idcliente']           
        finally:
            conn.connection.close()

        return result