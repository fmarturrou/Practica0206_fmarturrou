# Lista que almacenará los diccionarios de los alumnos
alumnos = []

while True:
    # Mostrar el menú de opciones
    print("\nMenú de opciones:")
    print("1. Añadir alumno/a")
    print("2. Eliminar alumno/a")
    print("3. Mostrar alumno/a")
    print("4. Listar todo el alumnado")
    print("5. Listar alumnado aprobado")
    print("6. Terminar")
    
    # Solicitar la opción al usuario
    opcion = input("Selecciona una opción (1-6): ")
    
    if opcion == "1":
        # Añadir alumno/a
        nif = input("Introduce el NIF del alumno/a: ")
        nombre = input("Introduce el nombre del alumno/a: ")
        apellidos = input("Introduce los apellidos del alumno/a: ")
        telefono = input("Introduce el teléfono del alumno/a: ")
        correo = input("Introduce el correo del alumno/a: ")
        aprobado = input("¿Ha aprobado el módulo? (True/False): ").lower() == "true"
        
        # Crear el diccionario del alumno
        alumno = {
            "nif": nif,
            "datos": {
                "nombre": nombre,
                "apellidos": apellidos,
                "telefono": telefono,
                "correo": correo,
                "aprobado": aprobado
            }
        }
        
        # Añadir el alumno a la lista de alumnos
        alumnos.append(alumno)
        print(f"Alumno/a {nombre} {apellidos} añadido/a con éxito.")
    
    elif opcion == "2":
        # Eliminar alumno/a
        nif = input("Introduce el NIF del alumno/a a eliminar: ")
        encontrado = False
        
        # Buscar el alumno por NIF y eliminarlo
        for alumno in alumnos:
            if alumno["nif"] == nif:
                alumnos.remove(alumno)
                encontrado = True
                print(f"Alumno/a con NIF {nif} eliminado/a con éxito.")
                break
        
        if not encontrado:
            print(f"No se ha encontrado ningún alumno/a con el NIF {nif}.")
    
    elif opcion == "3":
        # Mostrar alumno/a
        nif = input("Introduce el NIF del alumno/a a mostrar: ")
        encontrado = False
        
        # Buscar el alumno por NIF y mostrar sus datos
        for alumno in alumnos:
            if alumno["nif"] == nif:
                encontrado = True
                datos = alumno["datos"]
                print(f"\nDatos del alumno/a con NIF {nif}:")
                print(f"Nombre: {datos['nombre']}")
                print(f"Apellidos: {datos['apellidos']}")
                print(f"Teléfono: {datos['telefono']}")
                print(f"Correo: {datos['correo']}")
                print(f"Aprobado: {'Sí' if datos['aprobado'] else 'No'}")
                break
        
        if not encontrado:
            print(f"No se ha encontrado ningún alumno/a con el NIF {nif}.")
    
    elif opcion == "4":
        # Listar todo el alumnado
        print("\nListado de todo el alumnado:")
        if not alumnos:
            print("No hay alumnos en la base de datos.")
        else:
            for alumno in alumnos:
                datos = alumno["datos"]
                print(f"NIF: {alumno['nif']} | Nombre: {datos['nombre']} {datos['apellidos']}")
    
    elif opcion == "5":
        # Listar alumnado aprobado
        print("\nListado de alumnado aprobado:")
        if not alumnos:
            print("No hay alumnos en la base de datos.")
        else:
            aprobado_encontrado = False
            for alumno in alumnos:
                datos = alumno["datos"]
                if datos["aprobado"]:
                    aprobado_encontrado = True
                    print(f"NIF: {alumno['nif']} | Nombre: {datos['nombre']} {datos['apellidos']}")
            
            if not aprobado_encontrado:
                print("No hay alumnos aprobados en la base de datos.")
    
    elif opcion == "6":
        # Terminar el programa
        print("Terminando el programa...")
        break
    
    else:
        # Opción inválida
        print("Opción no válida. Por favor, elige una opción del 1 al 6.")