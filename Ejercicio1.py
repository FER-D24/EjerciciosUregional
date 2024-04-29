def productolistafor(lista):
  producto = 1
  for num in lista:
    producto *= num
  return producto

def productolistawhile(lista2):
  producto = 1
  x = 0
  while x < len(lista2):
    producto *= lista2[x]
    x += 1
  return producto

lista = [5, 10]
lista2 = (3,6,9)
resultado1 = productolistafor(lista)
resultado2 = productolistawhile(lista2)
print("El producto de los elementos en la lista es:", resultado1)
print("El producto de los elementos en la lista es:", resultado2)