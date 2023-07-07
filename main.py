# Traemos todas las funciones
from funciones import *

# Probando algunas funciones
a = leerArchivo('ejemplo1')
a = eliminarPuntuacion(a)
a = pasarAMinusculas(a)
a = eliminarSaltosDeLinea(a)
b = convertirALista(a)
b = eliminarCadenasVacias(b)
print(b)