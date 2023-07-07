import string

# Convertir de cadena de texto a lista
def convertir(texto):
    lista = list(texto.split(' '))
    return lista

# Leer un archivo de texto
def leer():
    texto = open('ejemplos/', 'r', encoding='utf-8')
    contenido = texto.read()
    texto.close()
    return contenido # Devolvemos el contenido en forma de cadena

# Eliminamos los simbolos de puntuación del texto
def eliminarPuntuacion(texto):
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    return texto
