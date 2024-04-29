# Usando un ciclo for
def sumarListaFor(lista):
  suma = 0
  for num in lista:
    suma += num
  return suma

# Usando un ciclo while
def sumarListaWhile(lista):
  suma = 0
  x = 0
  while x < len(lista): 
    suma += lista[x] 
    x += 1
  return suma

lista = [5, 10, 15, 50, 25]
resultado = sumarListaFor(lista)
print("La suma de los elementos en la lista es:", resultado)
