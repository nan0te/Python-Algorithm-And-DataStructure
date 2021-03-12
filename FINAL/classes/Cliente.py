class Cliente:
    def __init__(self, nombre, tel, direccion, dni):
        self.__Nombre = nombre
        self.__Tel = tel
        self.__Direccion = direccion
        self.__DNI = dni

    def getNombre(self):
        return self.__Nombre
    
    def getTel(self):
        return self.__Tel

    def getDireccion(self):
        return self.__Direccion

    def getDNI(self):
        return self.__DNI

    def setNombre(self, nombre):
        self.__Nombre = nombre

    def setTel(self, tel):
        self.__Tel = tel

    def setDireccion(self, direccion):
        self.__Direccion = direccion

    def setDNI(self, dni):
        self.__DNI = dni

        