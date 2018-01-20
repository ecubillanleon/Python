# -*- coding: utf-8 -*-

# Autor: Enmanuel Cubillan
# Bucle for en Python
# Verificación de correo electronico

contador = 0
correo = raw_input('Introduce tu correo: ')

for i in correo:
    if (i=='@') or (i=='.'):
        contador = contador+1
        
if contador == 2:
    print 'El email es correcto!',
else:
    print 'No es un correo valido!'
        
