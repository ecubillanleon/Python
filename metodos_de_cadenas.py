# -*- coding: utf-8 -*-

# Autor: Enmanuel Cubillan
# Métodos de cadenas

nombre_usuario = raw_input('Ingrese su nombre: ')
print('El nombre es: ',nombre_usuario.upper()) # convierte la cadena en mayusculas
print('El nombre es: ',nombre_usuario.lower()) # convierte la cadena en minusculas
print('El nombre es: ',nombre_usuario.capitalize()) # convierte la primera letra en mayuscula


edad = raw_input('\n\nIngrese su edad: ')

while(edad.isdigit() == False):
    print('Por favor introduce un valor numerico')
    edad = raw_input('Ingrese su edad: ')

    
if (int(edad) < 18):
    print('No puede pasar')
else:
    print('Puede pasar')
