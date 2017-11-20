# -*- coding: utf-8 -*-

# Autor: Enmanuel Cubillan
# Método de Burbuja

from random import randrange

def rellena (talla, rango):
    valores = [0] * talla
    for i in range(talla):
        valores[i] = randrange(0, rango)
    return valores

def burbuja (valores):
    nuevo = valores[:]
    for i in range(len(nuevo)):
        for j in range(len(nuevo)-1-i):
            if nuevo[j] > nuevo[j+1]:
                nuevo[j], nuevo[j+1] = nuevo[j+1], nuevo[j]
    return nuevo

# Programa principal
talla = 10
rango = 10

vector = rellena(talla, rango)

print 'Método de Burbuja'
print '\nVector desordenado:', vector
ordenado = burbuja(vector)
print 'Vector ordenado:', ordenado
