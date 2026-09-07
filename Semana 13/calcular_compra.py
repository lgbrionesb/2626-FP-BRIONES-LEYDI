"""Calcula el total de una compra mediante una funcion."""


def calcular_total(precio, cantidad):
    """Devuelve el total de la compra segun el precio y la cantidad."""
    total = precio * cantidad
    return total


if __name__ == "__main__":
    # Datos de ejemplo de una compra.
    precio_producto = 10
    cantidad_productos = 3

    resultado = calcular_total(precio_producto, cantidad_productos)
    print(f"El total de la compra es: ${resultado:.2f}")
