# TRABAJO 2do CUATRIMESTRE punto 2

#from Profesional import Profesional

#profesional  = Profesional('Nano Nobile', 'Av. Ketim POrta 666', 'FALSE', '39321123', '07/07/2000')

#print('Importe Total: ', profesional.calcularImportes(150))
#print('Importe Total: ', profesional.getTotalAPagar())

#profesional.muestra()

from ManagerUsers import ManagerUsers

manager_users = ManagerUsers()
manager_users.addProfesional('Nano Nobile', 'Av. Ketim POrta 666', 'FALSE', '39321123', '07/07/2000')
manager_users.addParticular('Nano Nobile', 'Av. Ketim POrta 666', 'FALSE', '39321122', '07/07/2000')
manager_users.addComercial('Nanote Nobile', 'Av. Ketim POrta 666', 'FALSE', '39321120', '07/07/2000')
manager_users.imprimirUsuarios()
manager_users.searchUser('Nanote Nobile')