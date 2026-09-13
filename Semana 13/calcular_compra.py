"""Calcula el total de una compra mediante una funcion."""


def calcular_total(precio, cantidad):
    """Devuelve el total de la compra segun el precio y la cantidad."""
    total = precio * cantidad
    return total


if __name__ == "__main__":
    # Se solicitan los datos de la compra al usuario.
    precio_producto = float(input("Ingrese el precio del producto: "))
    cantidad_productos = int(input("Ingrese la cantidad de productos: "))

    resultado = calcular_total(precio_producto, cantidad_productos)
    print(f"El total de la compra es: ${resultado:.2f}")
