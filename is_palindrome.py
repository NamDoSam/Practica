def invertir_frase(frase):
    frase_invertida = frase[::-1]
    if frase == frase_invertida:
        return True
    else:
        return False

print(invertir_frase('dondednod'))
print(invertir_frase('level'))
print(invertir_frase('cacatua'))
print(invertir_frase('locura'))