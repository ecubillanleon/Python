# -*- coding: utf-8  -*-

# Autor: Enmanuel Cubillan
# Creamos un programa para el uso del condicional if-while

opcion = 'z'

print 'Por favor seleccione una opción: \n'

while opcion <'a' or opcion >'c':
    print 'a) Adoro Python...'
    print 'b) Detesto Python...'
    print 'c) No se que es Python...'

    opcion = raw_input('\n> ')

    if opcion == 'a':
        print '\nQue bueno'

    elif opcion == 'b':
        print '\nQue mal'

    elif opcion == 'c':
        print '\nYa deberias saberlo'

    else:
        print '\nTu opcion no es válida...\n'
    
