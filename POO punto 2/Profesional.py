from Users import Users

class Profesional(Users):

    def __init__(self, name, address, baja, area, titulo):
        super().__init__(name, address, baja)
        self.Area = area
        self.Titulo = titulo
        self.AbonoFijo = 500
        self.TotalPagar = 0 
        
    
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

        self.TotalPagar = self.AbonoFijo + pulsos
        
        return self.TotalPagar
    
    def muestra(self):
        print('Nombre: ', self.Name)
        print('Direccion: ', self.Address)
        print('Baja: ', self.Baja)
        print('Area: ', self.Area)
        print('Titulo: ', self.Titulo)
        print('Abono fijo: ', self.AbonoFijo)
