from functools import reduce

lista_preciosMX = [1500, 2500, 3200, 4500, 6000, 1200, 8000]

promedio = reduce(lambda x, y: x + y, lista_preciosMX, 0)/ len(lista_preciosMX)

tipodecambio = 20
ventas_dolares = list(map(lambda pesos: pesos / tipodecambio, lista_preciosMX))

ventas_mayores_150 = list(filter(lambda dolares: dolares > 150, ventas_dolares))

suma_mayores_150 = reduce(lambda x, y: x + y, ventas_mayores_150, 0)

print(promedio)
print(ventas_dolares)
print(ventas_mayores_150)
print(suma_mayores_150)