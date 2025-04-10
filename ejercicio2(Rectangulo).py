class Rectangulo:
    def __init__(self, largo, ancho):
        """
        Constructor de la clase Rectangulo.

        Args:
            largo (float): El largo del rectángulo. Debe ser mayor que cero.
            ancho (float): El ancho del rectángulo. Debe ser mayor que cero.

        Raises:
            ValueError: Si el largo o el ancho inicial no son mayores que cero.
        """
        if largo > 0 and ancho > 0:
            self.__largo = largo  # Atributo privado
            self.__ancho = ancho  # Atributo privado
        else:
            raise ValueError("El largo y el ancho del rectángulo deben ser mayores que cero.")

    def cambiar_dimensiones(self, nuevo_largo, nuevo_ancho):
        """
        Cambia las dimensiones del rectángulo.

        Args:
            nuevo_largo (float): El nuevo largo del rectángulo.
            nuevo_ancho (float): El nuevo ancho del rectángulo.

        Raises:
            ValueError: Si el nuevo largo o el nuevo ancho no son mayores que cero.
        """
        if nuevo_largo > 0 and nuevo_ancho > 0:
            self.__largo = nuevo_largo
            self.__ancho = nuevo_ancho
            print(f"Dimensiones del rectángulo actualizadas a: Largo = {self.__largo:.2f}, Ancho = {self.__ancho:.2f}")
        else:
            raise ValueError("El nuevo largo y el nuevo ancho del rectángulo deben ser mayores que cero.")

    def calcular_area(self):
        """
        Calcula y devuelve el área del rectángulo.

        Returns:
            float: El área del rectángulo.
        """
        return self.__largo * self.__ancho

    def calcular_perimetro(self):
        """
        Calcula y devuelve el perímetro del rectángulo.

        Returns:
            float: El perímetro del rectángulo.
        """
        return 2 * (self.__largo + self.__ancho)

    def obtener_dimensiones(self):
        """
        Devuelve las dimensiones actuales del rectángulo.

        Returns:
            tuple: Una tupla que contiene el largo y el ancho actuales.
        """
        return self.__largo, self.__ancho

# Ejemplo  de la clase Rectangulo
if __name__ == "__main__":
    try:
        mi_rectangulo = Rectangulo(5.0, 3.0)
        print(f"Dimensiones iniciales: Largo = {mi_rectangulo.obtener_dimensiones()[0]:.2f}, Ancho = {mi_rectangulo.obtener_dimensiones()[1]:.2f}")
        print(f"Área: {mi_rectangulo.calcular_area():.2f}")
        print(f"Perímetro: {mi_rectangulo.calcular_perimetro():.2f}")

        mi_rectangulo.cambiar_dimensiones(7.5, 4.2)
        print(f"Nueva área: {mi_rectangulo.calcular_area():.2f}")
        print(f"Nuevo perímetro: {mi_rectangulo.calcular_perimetro():.2f}")

        print(f"Dimensiones actuales: Largo = {mi_rectangulo.obtener_dimensiones()[0]:.2f}, Ancho = {mi_rectangulo.obtener_dimensiones()[1]:.2f}")

        try:
            mi_rectangulo.cambiar_dimensiones(0, 5.0)
        except ValueError as e:
            print(f"Error al cambiar las dimensiones: {e}")

        try:
            otro_rectangulo = Rectangulo(-2.0, 4.0)
        except ValueError as e:
            print(f"Error al crear el rectángulo: {e}")

    except ValueError as e:
        print(f"Error general: {e}")