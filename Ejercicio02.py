diccionario = {}
nombre = input("Introduce tu nombre\n")
diccionario["nombre"] = nombre
edad = input("Introduce tu edad\n")
diccionario["edad"] = edad
dirección = input("Introduce tu dirección\n")
diccionario["dirección"] = dirección
teléfono = input("Introduce tu teléfono\n")
diccionario["teléfono"] = teléfono
print(f"{diccionario.get("nombre")} tiene {diccionario.get("edad")} años, vive en {diccionario.get("dirección")} y su número de teléfono es {diccionario.get("teléfono")}")