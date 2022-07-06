#Primero importar el modulo de subprocesos
import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile']).decode('utf-8').split('\n')

# Ahora hay que guardar el profile por convertir en lista
profile = [i.split(':')[1][1:-1] for i in data if 'All User Profile' in i]
for i in profile:
    #Correr el segundo comando para checar el password
    password = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    # Guardar passwords despues de convertirlas en lista
    password = [b.split(':')[1][1:-1] for b in password if 'key-content' in b]
    #Imprimir los perfiles(wifi nombres) con sus passwords usanto e intentando con el metodo de exepcion a mano
    try:
        print('{:<30} | {:<}'.format(i, password[0]))
    except IndexError:
        print('{:<30} | {:<}'.format(i, ''))

