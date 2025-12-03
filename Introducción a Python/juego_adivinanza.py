import random

numero_oculto = random.randint(0,100) #No considera el último número
intentos = 0
intentos_totales = 5
acierto = False

print('¡Adivina el número oculto!')
while not acierto and intentos < intentos_totales:
    entrada = input('Escribe cualquier número del 1 al 99 ') 
    numero = int(entrada) #Castear: convertir un string a número.
    #El input devuelve un string, tengo que convertirlo a número para que el código funcione
    if numero == numero_oculto:
        print('¡Muy bien! Adivinaste el número secreto :)')
        acierto = True
    elif numero < numero_oculto:
        print('No adivinaste el número oculto. Te doy una pista: es un número mayor al que elegiste.')
    else:
        print('No adivinaste el número oculto. Te doy una pista: es un número menor al que elegiste.')
    intentos += 1

if intentos <= intentos_totales:
    print('Ya no quedan intentos disponibles :(')




