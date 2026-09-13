"""Permite ingresar y mostrar una matriz de 5 filas por 5 columnas."""


if __name__ == "__main__":
    # Se crea una matriz de 5x5 inicializada con ceros.
    matriz = [[0 for _ in range(5)] for _ in range(5)]

    # Se solicitan y almacenan los 25 valores mediante bucles anidados.
    for fila in range(5):
        for columna in range(5):
            matriz[fila][columna] = int(
                input(f"Ingrese el valor para la posicion [{fila}][{columna}]: ")
            )

    print("\nMatriz ingresada:")

    # Se recorre la matriz y se muestran sus valores organizados por filas.
    for fila in matriz:
        for valor in fila:
            print(valor, end="\t")
        print()
