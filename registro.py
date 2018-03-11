# -*- coding: utf-8 -*-

# Autor: Enmanuel Cubillan
# Programa que registra una persona

print 'Registro de Persona'

for i in range(0,1):
    nombre = raw_input('\nIngrese su nombre: ')
    apellido = raw_input('Ingrese su apellido: ')
    cedula = int(raw_input('Ingrese su cédula: '))
    edad = int(raw_input('Ingrese su edad: '))
        

print '\nNombre          Apellido         Cédula        Edad'
print '_____________________________________________________'
for i in range(0,1):
    print '%s	%s	%s        %s' %(nombre,apellido,cedula,edad)
