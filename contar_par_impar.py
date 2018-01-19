# -*- coding: utf-8 -*-

# Autor: Enmanuel Cubillan
# Programa que cuenta la cantidad de números pares, impares o ceros

entrar = True
contar_par = 0
contar_impar = 0
contar_ceros = 0

print 'Programa que cuenta la cantidad de números pares, impares o ceros'

while(entrar):
    cantidad = int(raw_input('Ingrese la cantidad de números: '))

    for i in range(cantidad):
        numero = int(raw_input('Ingrese un número: '))

        if (numero >= 0):
            if ((numero %2 == 0) and (numero >= 1)):
                contar_par = contar_par + 1

            elif (numero %2 == 1):
                contar_impar = contar_impar + 1

            else:
                contar_ceros = contar_ceros + 1

        else:
            print 'Opción no válida.'
    entrar = False

print '___________________________________'
print 'Totales'
print '\nTotal de números %s' %(cantidad)
print 'Total de Pares %s' %(contar_par)
print 'Total de Impares %s' %(contar_impar)
print 'Total de Ceros %s' %(contar_ceros)
