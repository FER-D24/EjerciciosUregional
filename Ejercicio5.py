def EncontrarNumeroMayor(numeros):
    mayor = numeros[0]
    for numero in numeros:
        if numero > mayor:
            mayor = numero
    return mayor

numeros = []
for i in range(5):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

mayor = EncontrarNumeroMayor(numeros)
print("El número mayor es:", mayor)