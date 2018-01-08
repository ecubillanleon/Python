# -*- coding: utf-8 -*-

# Autor: Enmanuel Cubillan
# Programa que hace la sumatoria de las posiciones pares


suma = 0
print 'Sumatoria de Posiciones Pares'
tamano = int(raw_input('Ingrese la cantidad de elementos: '))

arreglo = [0 for i in range(tamano)]
for i in range(len(arreglo)):
    arreglo[i] = int(raw_input('Ingrese un número: '))

    if(i%2 != 0):
        suma = suma + arreglo[i]

print '\nLa suma de las posiciones pares es: %s' %(suma)
 
