import random
import time

def mostrarintroduccion():
    print("En un mundo, muy muy lejano, se encuentra la tierra de los Dragones;")
    print("en ella viven gran cantidad de dragones con mal caracter y hambrientos,")
    print("y otros muy amables y compasivos, los cuales estan dispuestos")
    print("a compartir sus riquesas y tesoros contigo.")
    print("Frente a ti se encuntran dos cuevas, en las cuales viven dos dragones.")
    print("En una cueva, el dragon que vive es muy feroz y hambriento,")
    print("si la cueva que eliges es la de él, se enfadará y te comerá de un solo bocado.")
    print("Por otro lado, su vecino es un dragon alegre y gentil el cual compartirá ")
    print("todos sus tesoros contibo\n")

def eligecueva():
    cueva = ''

    while cueva != '1' and cueva != '2':
        print('¿Qué cueva eliges para entrar? (1 o 2)')
        cueva = input()

    return cueva
def explorarcueva(cuevaelegida):
    print('Te estas aproximando a la cueva que elegiste...')
    time.sleep(2)
    print('La cueva es oscura y terrorífica|||')
    time.sleep(2)
    print('De repente y sorpresivamente aparece frente a ti un dragón con sus fauces abiertas..')

    cuevaAmigable = random.randint(1,2)

    if cuevaelegida == cuevaAmigable:
        print('Y te saluda, invitandote a pasar y a disfrutar de los tesoros acumulados|||')
    else:
        print(' y te come entero sin que te dieras cuenta siquiera de lo sucedido...')
    print()
    time.sleep(2)
jugarDeNuevo = 'si'
while jugarDeNuevo == 'si' or jugarDeNuevo == 's':
    mostrarintroduccion()

    numeroDeCueva = eligecueva()

    explorarcueva(numeroDeCueva)

    print('Quieres jugar de nuevo, ¿si o no?')
    jugarDeNuevo = input()

