
jugador1 = input("¿Piedra, papel o tijera? ")
jugador2 = input("¿Piedra, papel o tijera? ") 

condicion1 = jugador1 == "piedra" and jugador2 == "tijera"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijera" and jugador2 == "papel"

if jugador1 == jugador2:
    print("¡Empate!")
elif condicion1 or condicion2 or condicion3:
    print("Ganador: ¡Jugador 1!")
else:
    print("Ganador: ¡Jugador 2!")
                                                                                 
