# -*- coding: utf-8 -*-

# Autor: Enmanuel Cubillan
# Programa de registro de personas, además nos dice quien es el (la)\
# menor y el (la) mayor con respecto a su edades

nombre = [0 for x in range(0,3)]
edad = [0 for x in range(0,3)]
aux = [0 for x in range(0,3)]

for i in range(0,3):
    nombre[i] = (raw_input('Ingrese su nombre: '))
    edad[i] = int(raw_input('Ingrese su edad: '))
    print ''
    aux[i] =  edad[i]

    
for i in range(0,3):
    for j in range(0,2):
        if(aux[j] > aux[j+1]):
            mayor = aux[j]
            aux[j] = aux[j+1]
            aux[j+1] = mayor

      
print '_____________________________________________'
print 'Edad                         Nombre'
for i in range(0,3):
    for j in range(0,3):
        if(edad[j] == aux[i]):
            print ' %s \t\t\t%s' %(edad[j],nombre[j])

            if(i == 0):
                menor = j
            elif(i == 2):
                mayor = j


print '\n\nEl (La) menor es %s ' %(nombre[menor])
print 'El (La) mayor es %s ' %(nombre[mayor])
