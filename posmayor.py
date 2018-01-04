# -*- coding: utf-8 -*-

# Autor: Enmanuel Cubillan
# Programa que pide diez números al usuario, y nos dice cual
# es el mayor en que posición esta

posmayor = ''
numero = [0 for x in range(0,10)]

for i in range(0,10):
    numero[i] = int(raw_input('Ingrese un número: '))

mayor = numero[i]

for i in range(0,10):
    if(numero[i] > mayor):
        mayor = numero[i]
        posmayor = i

print '\nEl mayor es %s y esta en la posición %s' %(mayor,posmayor)
