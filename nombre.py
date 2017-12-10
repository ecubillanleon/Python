# -*- coding: utf-8 -*-

# Autor: Enmanuel Cubillan
# Funciones en Python

def nombre():
    mi_nombre = 'Enmanuel'
    return mi_nombre

print 'Nombre:', nombre()


def edad():
    edad = raw_input('Ingrese su edad: ')

    if edad >=18:
        print 'Eres mayor de edad'
    else:
        print 'Eres menor de edad'

edad()
