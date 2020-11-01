from Users import Users

class Particular(Users):

    def __init__(self, name, address, baja, dni, fechaNac):
        super().__init__(name, address, baja)
        self.__Name = self.Name
        self.__Address = self.Address
        self.__Baja = self.Baja
        self.__DNI = dni
        self.__fechaNacimiento = fechaNac
        self.__AbonoFijo = 300
        self.__TotalPagar = 0
        
    
    def calcularImportes(self, pulsos):
        try:
            if pulsos > 0 and pulsos <= 200:
                pulsos = pulsos *  0.5
            elif pulsos > 201 and pulsos <= 400:
                pulsos = pulsos *  0.7
            elif pulsos > 401 and pulsos <= 1000:
                pulsos = pulsos *  1.0
            elif pulsos < 1000:
                pulsos = pulsos *  1.2

        except ValueError:
            print('A ValueError occured!')

        self.__TotalPagar = self.__AbonoFijo + pulsos

        return self.__TotalPagar
    
    def getTotalAPagar(self):
        return self.__TotalPagar
    
    def getDNI(self):
        return self.__DNI

    def getName(self):
        return self.__Name

    def muestra(self):
        print('Nombre: ', self.__Name)
        print('Direccion: ', self.__Address)
        print('Baja: ', self.__Baja)
        print('DNI: ', self.__DNI)
        print('Fecha de Nacimiento: ', self.__fechaNacimiento)
        print('Abono fijo: ', self.__AbonoFijo)
        print('\n')


