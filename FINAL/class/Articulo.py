from Proveedor import Proveedor
from Stock import Stock

class Articulo:
    def __init__(self, id, nombre, descripcion, stock, Proveedor, Stock):
        self.__Id = id
        self.__Nombre = nombre
        self.__Descripcion = descripcion
        self.__Stock = Stock
        self.__NombreProveedor = Proveedor

    def getNombre(self):
        return self.__Nombre
    
    def getDescripcion(self):
        return self.__Descripcion

    def getStock(self):
        return self.__Stock.getStock()

    def getNombreProveedor(self):
        return self.__NombreProveedor.getNombre()

    def setNombre(self, nombre):
        self.__Nombre = nombre
    
    def setDescripcion(self, descripcion):
        self.__Descripcion = descripcion
    
    def setStock(self, stock):
        self.__Stock.Stock = stock

    def setNombreProveedor(self, nombre):
        self.__NombreProveedor.Nombre

     