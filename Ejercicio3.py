def numeromayor(lista, numero):
  for num in lista:
    if num > numero:
      print(num)

lista = [1,2,3,4,5,6,7,8,9,10]
numerodado = int(input("Ingrese un numero: "))
print("Los números mayores que", numerodado, "son:")
numeromayor(lista, numerodado)
