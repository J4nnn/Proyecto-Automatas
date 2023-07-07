import string
import unidecode # Se necesita instalar -> 'pip install Unidecode'
import re

# Convertir de cadena de texto a lista
def convertir(texto):
    lista = list(texto.split(' '))
    return lista

# Leer un archivo de texto
def leer(archivo):
    texto = open('ejemplos/{}.txt'.format(archivo), 'r', encoding='utf-8')
    contenido = texto.read()
    texto.close()
    return contenido # Devolvemos el contenido en forma de cadena

# Eliminar los simbolos de puntuación y acentos del texto
def eliminarPuntuacion(texto):
    texto = texto.translate(str.maketrans('', '', string.punctuation)) # Eliminamos puntuación
    texto = unidecode.unidecode(texto) # Eliminamos acentos
    # Notar que ¿ y ¡ son casos especiales del español y no se eliminan arriba
    texto = re.sub('[¿¡]', '', texto) # Eliminamos ¿ y ¡
    return texto
