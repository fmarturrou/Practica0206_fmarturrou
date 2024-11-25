monedas = {"Euro":"€", "Dolar":"$", "Yen":"¥"}
usuario = input("Escribe la primera moneda que se te ocurra\n").capitalize()
if usuario == "Euro":
    print(monedas["Euro"])
elif usuario == "Dolar":
    print(monedas["Dolar"])
elif usuario == "Yen":
    print(monedas["Yen"])
else:
    print("La moneda que has introducido no se corresponde a las del diccionario")