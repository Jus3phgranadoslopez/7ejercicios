class Producto:
    def __init__(self, nombre, precio):
        """
        Constructor de la clase Producto.

        Args:
            nombre (str): El nombre del producto.
            precio (float): El precio del producto. Debe ser mayor que cero.

        Raises:
            ValueError: Si el precio inicial no es mayor que cero.
        """
        self.__nombre = nombre  # Atributo privado (name mangling)
        if precio > 0:
            self.__precio = precio  # Atributo privado
        else:
            raise ValueError("El precio inicial del producto debe ser mayor que cero.")

    def cambiar_precio(self, nuevo_precio):
        """
        Cambia el precio del producto.

        Args:
            nuevo_precio (float): El nuevo precio del producto.

        Raises:
            ValueError: Si el nuevo precio no es mayor que cero.
        """
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
            print(f"El precio de '{self.__nombre}' ha sido actualizado a ${self.__precio:.2f}.")
        else:
            raise ValueError("El nuevo precio del producto debe ser mayor que cero.")

    def obtener_precio(self):
        """
        Obtiene el precio actual del producto.

        Returns:
            float: El precio actual del producto.
        """
        return self.__precio

    def obtener_nombre(self):
        """
        Obtiene el nombre del producto.

        Returns:
            str: El nombre del producto.
        """
        return self.__nombre

    def aplicar_descuento(self, porcentaje_descuento):
        """
        Aplica un descuento al precio del producto.

        Args:
            porcentaje_descuento (float): El porcentaje de descuento a aplicar (entre 0 y 100).

        Raises:
            ValueError: Si el porcentaje de descuento no está entre 0 y 100.
        """
        if 0 <= porcentaje_descuento <= 100:
            descuento = self.__precio * (porcentaje_descuento / 100)
            self.__precio -= descuento
            print(f"Se aplicó un descuento del {porcentaje_descuento:.2f}% a '{self.__nombre}'. Nuevo precio: ${self.__precio:.2f}.")
        else:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")

# Ejemplo de  la clase Producto
if __name__ == "__main__":
    try:
        mi_producto = Producto("Camiseta", 25.00)
        print(f"Nombre del producto: {mi_producto.obtener_nombre()}")
        print(f"Precio actual: ${mi_producto.obtener_precio():.2f}")

        mi_producto.cambiar_precio(28.50)

        mi_producto.aplicar_descuento(10)
        mi_producto.aplicar_descuento(20)

        try:
            mi_producto.cambiar_precio(0)
        except ValueError as e:
            print(f"Error al cambiar el precio: {e}")

        try:
            mi_producto.aplicar_descuento(110)
        except ValueError as e:
            print(f"Error al aplicar el descuento: {e}")

    except ValueError as e:
        print(f"Error al crear el producto: {e}")