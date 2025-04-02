import random

opciones = ("piedra","papel","tijera")
ejecutando = True

while ejecutando:
    jugador = None
    computador = random.choice(opciones)

    while jugador not in opciones:
        jugador = input("Ingresa tu opcion (piedra,papel,tijera): ")
    print(f"jugador: {jugador}")
    print(f"computador: {computador}")

    if jugador == computador:
        print("Empate")
    elif jugador == "piedra" and computador == "tijera":
        print("¡Ganaste!")
    elif jugador == "papel" and computador == "piedra":
        print("¡Ganaste!")
    elif jugador == "tijera" and computador == "papel":
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")
    jugar_denuevo = input("Jugar denuevo? (s/n): ").lower()
    if not jugar_denuevo == "s":
        ejecutando = False

print("¡Gracias por jugar!")
