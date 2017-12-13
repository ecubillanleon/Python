# -*- coding: utf-8 -*-
import math 

# Autor: Enmanuel Cubillan
# Bucle while en Python
# Raiz cuadrada de un número

print 'Programa de cálculo de raíz cuadrada'
numero = int(input('Introduce un número: '))

intentos = 0

while numero < 0:
    print 'La raíz cuadrada de un número negativo no existe!'

    if intentos == 2:
        print '\nHas consumido muchos intentos. \nEl programa a finalizado.'
        break;

    numero = int(input('\nIntroduce un número: '))
    if numero < 0:
        intentos = intentos + 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print 'La raíz cuadrada de ' + str(numero) + ' es %.4f' % (solucion)
