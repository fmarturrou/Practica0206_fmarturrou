diccionario = {"Pan": 1.40, "Huevos":2.30, "Cebolla": 0.85, "Aceite": 4.35}
artículo = input("Escribe un artículo de supermercado\n").capitalize()
unidades = int(input("¿Cuantas unidades quieres de ese artículo?\n"))
if artículo in diccionario:
    precio = diccionario[artículo] * unidades
    print(f"El precio de {unidades} unidades de {artículo} es de {precio}€")
else:
    print(f"El artículo {artículo} no está disponible en el diccionario.")