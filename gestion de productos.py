productos = ["Frijoles Refritos", "Coca Cola", "Zumo de Naranja", "Café de Olla", "Gorditas de Chicharrón", "Huevos Motuleños"]

productos_ordenados = sorted(productos)

cadena_ordenada = ", ".join(productos_ordenados)

slugs = list(map(lambda nombre: nombre.lower().replace(" ", "-"), productos_ordenados))

print(slugs)

print(cadena_ordenada)