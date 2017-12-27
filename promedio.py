# -*- coding: utf-8 -*-

# Autor: Enmanuel Cubillan
# Programa que calcula el promedio de notas de un estudiante

suma = 0
opcion = 1
cantidad_de_materias = 0
promedio_total = 0

nombre = raw_input('Nombre del estudiante: ')
carnet = int(raw_input('Número de carnet: '))

while(opcion == 1):
    materia = raw_input('\nIngrese el nombre de la materia: ')
    cantidad_de_materias = cantidad_de_materias + 1
    cantidad_de_notas = int(raw_input('Ingrese la cantidad de notas: '))

    for i in range(cantidad_de_notas):
        nota = int(raw_input('Ingrese la nota de la materia: '))
        suma = suma + nota

    promedio = (suma / cantidad_de_notas)

    print '\nLa nota final de %s es %.2f' %(materia,promedio)
    print '\nDesea ingresar otra materia \n1.- Si \n0.- No '
    opcion = int(raw_input('> '))

    while(opcion != 0 and opcion != 1):
        print '\nOpción no válida.\n'
        opcion = int(raw_input('> '))

if(opcion == 0):
    print '\nNombre del estudiante: %s' %(nombre)
    print 'Número de carnet: %s' %(carnet)

    promedio_total = (promedio_total + promedio) / cantidad_de_materias

    print 'El promedio total es %.2f' %(promedio_total)
