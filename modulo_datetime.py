import datetime

ahora = datetime.datetime.now()

print(ahora)
print(ahora.strftime('%d/%m/%Y %H:%M:%S')) #SI LA Y DE YEARS VA EN MAYUSCULAS MUESTRA LOS 4 DIGITOS DEL AÑO, SINO SOLO 2
