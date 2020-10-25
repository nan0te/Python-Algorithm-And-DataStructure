from Users import Users

class Particular(Users):

    def __init__(self, name, address, baja, dni, fechaNac):
        super().__init__(name, address, baja)
        self.DNI = dni
        self.fechaNacimiento = fechaNac
        self.AbonoFijo = 300
        self.TotalPagar = 0
        
    
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

        self.TotalPagar = self.AbonoFijo + pulsos

        return self.TotalPagar

    def muestra(self):
        print('Nombre: ', self.Name)
        print('Direccion: ', self.Address)
        print('Baja: ', self.Baja)
        print('DNI: ', self.DNI)
        print('Fecha de Nacimiento: ', self.fechaNacimiento)
        print('Abono fijo: ', self.AbonoFijo)


