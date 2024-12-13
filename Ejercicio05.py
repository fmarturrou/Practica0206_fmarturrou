diccionario = {}
terminar = "terminar"
palabras = ""

while palabras != terminar:
    palabras = str(input("Escribe palabras en español con su simil en inglés de esta manera: palabra:word, para acabar, ecribe terminar\n"))
    clave, valor = palabras.split(":")
    diccionario[clave] = valor
    print(diccionario)
