# juego.py
import random

MINIMO = 1
MAXIMO = 10

def adivinar():
    intentos = 3
    num = random.randint(MINIMO, MAXIMO)
    
    while intentos > 0:
        intento = int(input(f"Adivina el número entre {MINIMO} y {MAXIMO}. Te quedan {intentos} intentos: "))
        if intento < MINIMO or intento > MAXIMO:
            print(f"Por favor, introduce un número entre {MINIMO} y {MAXIMO}.")
            continue
        if intento == num:
            print("¡Felicidades! ¡Has adivinado el número!")
            break
        elif intento < num:
            print("El número es mayor.")
        else:
            print("El número es menor.")
        intentos -= 1
    else:
        print(f"Lo siento, has agotado tus intentos. El número era {num}.")

