# -*- coding: utf-8 -*-

# Autor: Enmanuel Cubillan
# Programa que calcula el factorial de un nuḿero

"""
Simple código que devuelve el factorial de un numero dado
Para calcular dicho valor, hay que multiplicar el numero dado, por su
antecesor mientas sea superior a 1

Ejemplo del factorial de 5 seria:

	5 * 4 * 3 * 2 * 1  = 120
"""

def factorial(x,n):
    
    """
    Función recursiva que calcula el factorial
    Tiene que recibir:
        x=>El ultimo valor calculado
    	n=>El numero a multiplicar
    """

    if(n>0):
	# Se va llamando a ella misma mientras el valor sea superior a 0
        x=factorial(x,n-1)
        x=x*n
        
    else:
        x=1

    return x
    
try:
    numero = int(raw_input("Inserta un número: "))

    # Ejecutamos la función recusiva para el calculo

    calculo=factorial(1,numero)

    print "El factorial de %s es %s" % (numero,calculo)

except:
    print "\nTiene que ser un valor númerico"






