

class Articulo:
    def __init__(self, nombre, descripcion, stock, proveedor, precio):
        
        self.__Nombre = nombre
        self.__Descripcion = descripcion
        self.__Stock = stock
        self.__NombreProveedor = proveedor
        self.__Precio = precio

    def getNombre(self):
        return self.__Nombre
    
    def getDescripcion(self):
        return self.__Descripcion

    def getStock(self):
        return self.__Stock

    def getNombreProveedor(self):
        return self.__NombreProveedor

    def getPrecio(self):
        return self.__Precio

    def setNombre(self, nombre):
        self.__Nombre = nombre
    
    def setDescripcion(self, descripcion):
        self.__Descripcion = descripcion
    
    def setStock(self, stock):
        self.__Stock = stock

    def setNombreProveedor(self, nombre):
        self.__NombreProveedor = nombre

    def setPrecio(self, precio):
        self.__Precio = precio 