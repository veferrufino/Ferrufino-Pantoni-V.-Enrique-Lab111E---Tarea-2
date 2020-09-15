'''
Ejercicio Nº1
Estudiante: Ferrufino Pantoni Victor Enrique  2LAB-111E"
'''
# Ingrese un tiempo X que estará representado en segundos, luego ingrese el tiempo que
# tomará en realizarse una tarea Z representado en segundos, minutos y horas. Se pide
# verificar si con el tiempo X se puede finalizar la tarea Z.

x=float(input('Dame el tiempo en segundos para finalizar la tarea -> '))

hrs=float(input('La tarea toma un tiempo en horas de -> '))
min=float(input('¿Con cuántos minutos? -> '))
seg=float(input('¿Y con cuantos segundos? -> '))

hrs=hrs*3600
min=min*60

z=hrs+min+seg

print('La tarea toma un tiempo de ',z,'seg y para finalizar la tarea necesitas un tienes de ',x,'seg. Por lo tanto...')
if (x>z):
    print('Tienes tiempo de sobra para finalizar la tarea.')
elif (x==z):
    print('Tienes en tiempo justo para finalizar la tarea.')
else:
    print('No alcanza el tiempo para finalizar la tarea.')

