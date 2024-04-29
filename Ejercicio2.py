def contar_paresFor(lista):
  contador_for = 0
  for numero in lista:
    if numero % 2 == 0:
      contador_for += 1
      print(numero)
  return contador_for

def contar_paresWhile(lista):
  contador_while = 0
  x = 0
  while x < len(lista):
    if lista[x] % 2 == 0:
      contador_while += 1
      print(lista[x])
    x += 1
  return contador_while

lista = (1,2,3,4,5,6,7,8,9,10)
print("los números pares son:", contar_paresFor(lista))
print("los números pares son:", contar_paresWhile(lista))
