import random
print('Lanzare una moneda al aire 1000 veces, adivina cuantas veces salio cara?')
print('Dale enter para iniciar')
input()
saliocara = 0
conteo = 0
while conteo < 1000:
    moneda = random.randint(0,1)
    if moneda == 1:
        saliocara = saliocara + 1
    conteo += 1
    if conteo == 100:
        print(f'En 100 tiradas, salieron {saliocara} veces cara ')
    if conteo == 500:
        print(f'A la mitad del juego ha salido {saliocara} veces cara')
print('Dime cuantas veces crees que salio cara al finalizar los 1000 intentos?')
monedacara = int(input())
if saliocara == monedacara:
    print('Excelente, Felicitaciones, acertaste!!!')
else:
    print(f'No, lo siento fueron {saliocara} veces')

