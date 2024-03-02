import random

RangoI = int(input("Ingresa el inicio del rango: "))
RangoF = int(input("Ingresa el fin del rango: "))
cantidad = int(input("Ingresa la cantidad de numeros: "))

numeros_aleatorios = [random.randint(RangoI, RangoF) for _ in range(cantidad)]

print("Numeros aleatorios generados:")
for numero in numeros_aleatorios:
    print(numero)