def contarVocales(cadena):
  vocales = "aeiouAEIOU"
  contador = 0
  for letra in cadena:
    if letra in vocales:
      contador += 1
  return contador

cadena = "Hola Mundo"
resultado = contarVocales(cadena)
print("La cantidad de vocales en la cadena es:", resultado)
