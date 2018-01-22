# -*- coding: utf-8 -*-

# Autor: Enmanuel Cubillan
# Bucle while en Python

edad = int(input('Introduce tu edad: '))

while ((edad < 0) or (edad > 100)):
    print 'Has introducido una edad incorrecta\n'
    edad = int(input('Introduce tu edad: '))

print 'La edad es: '  + str(edad)
