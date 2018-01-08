# -*- coding: utf-8 -*-

# Autor: Enmanuel Cubillan
# Leyendo archivos, ruta relativa y ruta absoluta

# Modos para abrir un archivo

"""
Modo de sólo lectura (r).\
En este caso no es posible realizar modificaciones sobre el archivo, solamente \
leer su contenido.

Modo de sólo escritura (w).\
En este caso el archivo es truncado (vaciado) si existe, y se lo crea si no \
existe.

Modo sólo escritura posicionándose al final del archivo (a).\
En este caso se crea el archivo, si no existe, pero en caso de que exista se \
posiciona al final, manteniendo el contenido original.
"""
#texto = open("prueba.txt")
#print(texto.read())

# Ruta relativa
texto = open("documentos/prueba.txt")
print(texto.read())


# Ruta absoluta
texto = open("documentos/docs/prueba.txt")
print(texto.read())
