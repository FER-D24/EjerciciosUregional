def ContarNombreMasLargo(nombres):
  NombreMasLargo = " "
  for nombre in nombres:
    if len(nombre) > len(NombreMasLargo):
      NombreMasLargo = nombre
  return NombreMasLargo

nombres = []
for i in range(5):
  nombre = input("Ingrese un nombre: ")
  nombres.append(nombre)

NombreMasLargo = ContarNombreMasLargo(nombres)
print("El nombre mas largo es", NombreMasLargo)
