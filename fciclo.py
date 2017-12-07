# -*- coding: utf-8 -*-

# Autor: Enmanuel Cubillan
# Programa que muestra el ciclo comprendido entre dos números

def fciclo(num1, num2):
    for i in range(num1,num2):
        print 'El ciclo es: ' +str(i)


n1 = int(raw_input('Ingrese un número: '))
n2 = int(raw_input('Ingrese un número: '))
print ''

fciclo(n1,n2)
