# Ejercicio 11: Agenda telefónica

agenda = {}  # Diccionario vacío para guardar los contactos

while True:
    print("\n--- Menú de Agenda ---")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")
    opcion = input("Elegir una opción: ")

    if opcion == "1":
        nombre = input("Nombre del contacto: ")
        telefono = input("Teléfono del contacto: ")
        agenda[nombre] = telefono
        print("Contacto agregado.")

    elif opcion == "2":
        nombre = input("Nombre del contacto a borrar: ")
        if nombre in agenda:
            del agenda[nombre]
            print("Contacto borrado.")
        else:
            print("Este contacto no existe.")

    elif opcion == "3":
        if agenda:
            print("\nContactos guardados:")
            for nombre, telefono in agenda.items():
                print(f"{nombre}: {telefono}")
        else:
            print("No hay contactos guardados.")

    elif opcion == "4":
        print("Saliendo de la agenda...")
        break

    else:
        print("Opción no válida, intentá de nuevo.")