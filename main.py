# Traemos todas las funciones
from funciones import *

# Tratamos el archivo de texto
a = leerArchivo('ejemplo5')
a = eliminarPuntuacion(a)
a = pasarAMinusculas(a)
a = eliminarSaltosDeLinea(a)
b = convertirALista(a)
b = eliminarCadenasVacias(b)
# print(b)

puntosSPAM = 0; # Si es mayor o igual a 7 se considerará SPAM
for i in range(0, len(b)):
    if evaluar(b[i]):
        puntosSPAM += 1

# Definimos si un correo es potencialmente SPAM
if puntosSPAM >= 7:
    print('El correo evaluado es potecialmente SPAM.')
else:
    print('El correo evaluado no es SPAM')