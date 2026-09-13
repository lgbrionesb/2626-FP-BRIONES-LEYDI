"""Declara y muestra una matriz de 3 filas por 3 columnas."""


if __name__ == "__main__":
    # Matriz de 3x3 con numeros enteros.
    matriz = [
        [2, 4, 6],
        [1, 3, 5],
        [7, 8, 9],
    ]

    print("Matriz 3x3:")

    # Se recorren las filas y columnas con ciclos anidados.
    for fila in matriz:
        for valor in fila:
            print(valor, end=" ")
        print()
