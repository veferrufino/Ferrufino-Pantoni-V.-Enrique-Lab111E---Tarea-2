# Ejercicio Nº2
# Utilizando los coeficiente (a,b,c) de una ecuacion de segundo grado se pide
# mostrar la naturaleza de sus raices.

''' Estudiante: Ferrufino Pantoni Victor Enrique Lab-111 '''

import math

a = float(input('El valor de a -> '))
b = float(input('El valor de b -> '))
c = float(input('El valor c -> '))

discr = (b**2 - 4*a*c)

if (discr>=0) and (a!=0):
    x1 = (-b + math.sqrt(discr)) / (2*a)
    x2 = (-b - math.sqrt(discr)) / (2*a)
    print('La primera raíz -> x1 = ',x1)
    print('La segunda raíz -> x2 = ',x2)
else:
    print('No existen raíces reales')