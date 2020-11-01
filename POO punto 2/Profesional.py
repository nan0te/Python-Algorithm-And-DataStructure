from Users import Users

class Profesional(Users):

    def __init__(self, name, address, baja, area, titulo):
        super().__init__(name, address, baja)
        self.__Name = self.Name
        self.__Address = self.Address
        self.__Baja = self.Baja
        self.__Area = area
        self.__Titulo = titulo
        self.__AbonoFijo = 500
        self.__TotalPagar = 0 
        
    
    def calcularImportes(self, pulsos):
        try:
            if pulsos > 0 and pulsos <= 250:
                pulsos = pulsos *  0.7
            elif pulsos > 251 and pulsos <= 500:
                pulsos = pulsos *  1.1
            elif pulsos > 501 and pulsos <= 1000:
                pulsos = pulsos *  1.3
            elif pulsos < 1000:
                pulsos = pulsos *  1.5

        except ValueError:
            print('A ValueError occured!')

        self.__TotalPagar = self.__AbonoFijo + pulsos
        
        return self.__TotalPagar
    
    def getTotalAPagar(self):
        return self.__TotalPagar

    def getName(self):
        return self.__Name
    
    def muestra(self):
        print('Nombre: ', self.__Name)
        print('Direccion: ', self.__Address)
        print('Baja: ', self.__Baja)
        print('Area: ', self.__Area)
        print('Titulo: ', self.__Titulo)
        print('Abono fijo: ', self.__AbonoFijo)
        print('\n')
