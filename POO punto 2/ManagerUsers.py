
from Profesional import Profesional
from Particular import Particular
from Comercial import Comercial


class ManagerUsers:
    userslist = []

    def addProfesional(self, name, address, baja, area, titulo):
        profesional = Profesional(name, address, baja, area, titulo)
        self.userslist.append(profesional)

    def addParticular(self, name, address, baja, dni, fechaNac):
        particular = Particular(name, address, baja, dni, fechaNac)
        self.userslist.append(particular)

    def addComercial(self, name, address, baja, rubro, cuilt):
        comercial = Comercial(name, address, baja, rubro, cuilt)
        self.userslist.append(comercial)
    
    def searchUser(self, name):
        for user in self.userslist:
            if name == user.getName():
                user.muestra()

    def imprimirUsuarios(self):
        for user in self.userslist:
	        user.muestra()
            
        
