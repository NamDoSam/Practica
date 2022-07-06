#adivina el numero
import random

intentosRealizados = 0

print("!Hola| ¿Como te llamas?")
miNombre = input()

numero = random.randint(1, 20)
print("Bueno, " + miNombre + ", estoy pensando en un numero entre 1 y 20.")

while intentosRealizados < 6:
    print("Intenta adivinar. ")
    estimacion = input()
    estimacion = int(estimacion)
    intentosRealizados = intentosRealizados + 1

    if estimacion < numero:
        print("Tu número es menor.")
    if estimacion > numero:
        print("Tu número es mayor.")
    if estimacion == numero:
        print("Felicitaciones!!! " + miNombre + " has adivinado el número en " + str(intentosRealizados) + " intentos!!")
        break
if estimacion != numero:
    numero = str(numero)
    print("Pues NO. El número que estaba pensado era " + numero)
