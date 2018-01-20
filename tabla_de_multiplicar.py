# -*- coding: utf-8 -*-

# Autor: Enmanuel Cubillan
# Programa que muestra la tabla de multiplicar de cualquier número
# Bucle For In

numero = int(raw_input('Ingrese un número: '))

print '\nTabla de Multiplicar\n\n ' + str(numero)
print '____________'
for i in [1,2,3,4,5,6,7,8,9,10]:
    print '%d x %d = %d' %(i,numero,i*numero)
