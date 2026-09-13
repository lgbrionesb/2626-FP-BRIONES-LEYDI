"""Gestiona la reserva de un asiento en una sala de cine."""


if __name__ == "__main__":
    # La matriz representa 3 filas por 4 columnas.
    # 0 significa asiento libre y 1 significa asiento reservado.
    asientos = [[0 for _ in range(4)] for _ in range(3)]

    # Se solicitan indices validos para la fila y la columna.
    while True:
        fila = int(input("Ingrese la fila del asiento (0 a 2): "))
        columna = int(input("Ingrese la columna del asiento (0 a 3): "))

        if 0 <= fila < 3 and 0 <= columna < 4:
            break

        print("Ubicacion invalida. Intente nuevamente.")

    # Se marca el asiento seleccionado como reservado.
    asientos[fila][columna] = 1

    # Se muestra la sala completa mediante bucles anidados.
    print("\nEstado de la sala:")
    for fila_actual in asientos:
        for estado in fila_actual:
            print(estado, end=" ")
        print()
