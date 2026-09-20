"""Calcula el promedio de tres notas mediante una funcion."""


def calcular_promedio(nota1, nota2, nota3):
    """Devuelve el promedio de tres notas."""
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio


def solicitar_nota(numero):
    """Solicita una nota valida entre 0 y 10."""
    while True:
        entrada = input(f"Ingrese la nota {numero} (0 a 10): ").strip()
        try:
            nota = float(entrada.replace(",", "."))
        except ValueError:
            print("Error: ingrese un numero valido.")
            continue

        if 0 <= nota <= 10:
            return nota

        print("Error: la nota debe estar entre 0 y 10.")


if __name__ == "__main__":
    print("Calculo del promedio de tres notas")
    primera_nota = solicitar_nota(1)
    segunda_nota = solicitar_nota(2)
    tercera_nota = solicitar_nota(3)

    resultado = calcular_promedio(primera_nota, segunda_nota, tercera_nota)
    print(f"El promedio final es: {resultado:.2f}")
