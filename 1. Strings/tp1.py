
print ("hello world!")

# 1. sustituir espacios en blancos por asteriscos

# txt = "primeras lineas en python"
# result = txt.replace(" ","*")
# print(result)

# 2. Leer el nombre y los 2 apellidos de una persona ( en 3 cadenas de caracteres diferentes)
#    y unirlo en una unica cadena. Luego muestre:
#   la cadena resultante - la cantidad de caracteres cad resultante -  convertir todo a may y min 
#   verificar si la cad fernandez se encuentra en el texto - mostrr en may la primera lentra de cada palabra

name = input('Enter your name: ')
lastname1 = input('Enter your last name: ')
lastname2 = input('Enter your other last name: ')

result = name + lastname1 + lastname2
_len = len(result)
output = 'Length of result is: ' + str(_len)

print(output)

print( result.upper() ) 
print( result.lower() )

_find = result.find('Fernandez')

if _find > 0:
    print('Fernandez is in the text')
else:
    print('Fernandez is not in the text')


# 3. Leer name y un caracter y comprobar si ese caracter esta en su nombre

name = input('Enter your name: ')
char = input('Enter the char: ')

result = char in name

print(result)




# 4. Leer una cadena donde en lugar de ñ se utiizo ny. Crear nueva cadena sustituyendo ny por ñ

char = input('Enter characters: ')
result = char.replace('ny','ñ')

if char in 'ñ':
    print(result)
else:
    print('\n')



#5. leer un String alrevez

def translateString(ch):
    return ch[::-1] 

char = input('Enter the characters: ')
result = translateString(char)

print(result)






