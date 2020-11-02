from Users import Users

class Comercial(Users):

    def __init__(self, name, address, baja, rubro, cuilt):
        super().__init__(name, address, baja)
        self.__Name = self.Name
        self.__Address = self.Address
        self.__Baja = self.Baja
        self.__Rubro = rubro
        self.__CUILT = cuilt
        self.__AbonoFijo = 700
        self.__TotalPagar = 0
        
    
    def calcularImpuestos(self, pulsos):
        try:
            if pulsos > 0 and pulsos <= 300:
                pulsos = pulsos *  0.9
            elif pulsos > 301 and pulsos <= 600:
                pulsos = pulsos *  1.2
            elif pulsos > 601 and pulsos <= 1000:
                pulsos = pulsos *  1.5
            elif pulsos < 1000:
                pulsos = pulsos *  1.7

        except ValueError:
            print('A ValueError occured!')

        self.__TotalPagar = self.__AbonoFijo + pulsos
        
        return self.__TotalPagar

    def setAddress(self, address):
        self.__Address = address
    
    def setBaja(self, baja):
        self.__Baja

    def getTotalAPagar(self):
        return self.__TotalPagar

    def getCuilt(self):
        return self.__CUILT
    
    def getName(self):
        return self.__Name

    def muestra(self):
        print('Nombre: ', self.__Name)
        print('Direccion: ', self.__Address)
        print('Baja: ', self.__Baja)
        print('Rubro: ', self.__Rubro)
        print('CUILT: ', self.__CUILT)
        print('Abono fijo: ', self.__AbonoFijo)
        print('\n')