from Users import Users

class Comercial(Users):

    def __init__(self, name, address, baja, rubro, cuilt):
        super().__init__(name, address, baja)
        self.Rubro = rubro
        self.CUILT = cuilt
        self.AbonoFijo = 700
        self.TotalPagar = 0
        
    
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

        self.TotalPagar = self.AbonoFijo + pulsos
        
        return self.TotalPagar

    def muestra(self):
        print('Nombre: ', self.Name)
        print('Direccion: ', self.Address)
        print('Baja: ', self.Baja)
        print('Rubro: ', self.Rubro)
        print('CUILT: ', self.CUILT)
        print('Abono fijo: ', self.AbonoFijo)