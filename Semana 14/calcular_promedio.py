"""Calcula el promedio de tres notas mediante una funcion."""


def calcular_promedio(nota1, nota2, nota3):
    """Devuelve el promedio de tres notas."""
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio


if __name__ == "__main__":
    print("Calculo del promedio de tres notas")
    primera_nota = float(input("Ingrese la primera nota: "))
    segunda_nota = float(input("Ingrese la segunda nota: "))
    tercera_nota = float(input("Ingrese la tercera nota: "))

    resultado = calcular_promedio(primera_nota, segunda_nota, tercera_nota)
    print(f"El promedio final es: {resultado:.2f}")
