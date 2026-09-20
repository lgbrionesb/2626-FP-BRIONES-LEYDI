"""Administra contactos usando un diccionario."""


def buscar_contacto(contactos, nombre):
    """Devuelve la clave del contacto sin distinguir mayusculas."""
    nombre_buscado = nombre.casefold()
    for nombre_guardado in contactos:
        if nombre_guardado.casefold() == nombre_buscado:
            return nombre_guardado
    return None


def agregar_contacto(contactos):
    """Solicita y agrega un contacto al diccionario."""
    nombre = input("Ingrese el nombre: ").strip()
    if not nombre:
        print("Error: el nombre no puede estar vacio.")
        return

    if buscar_contacto(contactos, nombre) is not None:
        print("Ya existe un contacto con ese nombre.")
        return

    telefono = input("Ingrese el numero telefonico: ").strip()
    if not telefono:
        print("Error: el numero telefonico no puede estar vacio.")
        return

    contactos[nombre] = telefono
    print(f"Contacto '{nombre}' agregado correctamente.")


def mostrar_contactos(contactos):
    """Muestra todos los contactos almacenados."""
    if not contactos:
        print("No hay contactos registrados.")
        return

    print("\nLista de contactos:")
    for nombre, telefono in contactos.items():
        print(f"- {nombre}: {telefono}")


def buscar_y_mostrar_contacto(contactos):
    """Busca un contacto por nombre y muestra su telefono."""
    nombre = input("Ingrese el nombre que desea buscar: ").strip()
    nombre_guardado = buscar_contacto(contactos, nombre)

    if nombre_guardado is None:
        print("No se encontro el contacto.")
    else:
        print(f"{nombre_guardado}: {contactos[nombre_guardado]}")


def eliminar_contacto(contactos):
    """Elimina un contacto del diccionario."""
    nombre = input("Ingrese el nombre que desea eliminar: ").strip()
    nombre_guardado = buscar_contacto(contactos, nombre)

    if nombre_guardado is None:
        print("No se encontro el contacto.")
    else:
        del contactos[nombre_guardado]
        print(f"Contacto '{nombre_guardado}' eliminado correctamente.")


def mostrar_menu():
    """Imprime las opciones disponibles."""
    print("\nAdministracion de contactos")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")


def main():
    contactos = {}

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            agregar_contacto(contactos)
        elif opcion == "2":
            mostrar_contactos(contactos)
        elif opcion == "3":
            buscar_y_mostrar_contacto(contactos)
        elif opcion == "4":
            eliminar_contacto(contactos)
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opcion no valida. Seleccione una opcion del 1 al 5.")


if __name__ == "__main__":
    main()
