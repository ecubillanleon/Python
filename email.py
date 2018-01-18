# -*- coding: utf-8 -*-

# Autor: Enmanuel Cubillan
# Bucle for en Python
# Verificación de correo electronico

valido = False
email = raw_input('Introduce tu correo: ')

for i in range(len(email)):
    if email[i] == '@':
        valido = True

if valido:
    print 'Correo valido!'
else:
    print 'Correo no valido!'
