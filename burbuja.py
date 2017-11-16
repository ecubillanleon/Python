# -*- coding: utf-8 -*-

# Autor: Enmanuel Cubillan
# Recorrido de una lista
# Método de Burbuja

# creamos una lista
lista = [2,4,6,3,8]
print 'Lista desordenada: ' + str(lista)

for recorrido in range(1,len(lista)):
    for posicion in range(len(lista) - recorrido):
        if lista[posicion] > lista[posicion + 1]:
            temp = lista[posicion]
            lista[posicion] = lista[posicion + 1]
            lista[posicion + 1] = temp

print 'Lista ordenada: ' + str(lista)
