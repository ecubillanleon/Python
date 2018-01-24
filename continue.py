# -*- coding: utf-8 -*-

# Autor: Enmanuel Cubillan
# continue - pass - else

for letra in 'Python':
    if letra == 'h':
        continue
    
    print 'Viendo la letra: ' + str(letra)

nombre = 'Enmanuel Cubillan'
contador = 0

for i in nombre:
    if i == ' ':
        continue
    contador+=1
    
print 'Longitud de la cadena ' + str(nombre) + ' es: ' + str(contador)
