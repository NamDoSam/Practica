#revertir una cadena de caracteres

cadena = 'El tiempo lo dirá'

for i in range(len(cadena) -1,-1,-1):
  print(cadena[i], end = '')

print()

print(cadena[::-1])