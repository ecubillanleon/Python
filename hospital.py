# -*- coding: utf-8 -*-

# Autor: Enmanuel Cubillan
# Programa que calcula el pago del hospital

repetir = 1

while(repetir == 1):
    paciente = raw_input('Ingrese el nombre del paciente: ')
    tipo_enfermedad = int(raw_input('Ingrese el tipo de enfermedad: '))
    dias_hospitalizado = int(raw_input('Ingrese los dias que el paciente ha estado hospitalizado: '))

    while(tipo_enfermedad < 1 or tipo_enfermedad > 3):
        print '\nEl tipo de enfermedad es invalido.'
        tipo_enfermedad = int(raw_input('Ingrese el tipo de enfermedad: '))
        
    if(tipo_enfermedad == 1):
        pago = dias_hospitalizado * 1500

    if(tipo_enfermedad == 2):
        pago = dias_hospitalizado * 1700        

    if(tipo_enfermedad == 3):
        pago = dias_hospitalizado * 1900

    print '\n\nEl paciente %s, que estuvo hospitalizado %s dias, \
con el tipo de enfermedad %s, debe pagar un total de %s Bsf por los \
servicios prestados.' %(paciente,dias_hospitalizado,tipo_enfermedad,pago)

    print '\n\nDesea ingresar otro paciente \n1.- Si \n0.- No '
    opcion = int(raw_input('> '))

    while(opcion != 0 and opcion != 1):
        print '\nOpción no válida.\n'
        opcion = int(raw_input('> '))

    if(opcion == 0):
        print '\nHasta pronto...'
        repetir = 0

    
