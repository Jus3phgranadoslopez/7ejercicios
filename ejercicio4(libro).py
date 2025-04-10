class Libro:
    def __init__(self, titulo, autor, total_paginas):
        """
        Constructor de la clase Libro.

        Args:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            total_paginas (int): El número total de páginas del libro.

        Raises:
            ValueError: Si el número total de páginas no es un entero positivo.
        """
        self.__titulo = titulo  # Atributo privado
        self.__autor = autor    # Atributo privado
        if isinstance(total_paginas, int) and total_paginas > 0:
            self.__total_paginas = total_paginas  # Atributo privado
        else:
            raise ValueError("El número total de páginas debe ser un entero positivo.")
        self.__pagina_actual = 1  # Atributo privado: Inicialmente en la página 1

    def avanzar_pagina(self, num_paginas):
        """
        Avanza un número de páginas en el libro.

        Args:
            num_paginas (int): El número de páginas a avanzar.

        Raises:
            ValueError: Si se intenta avanzar más allá del número total de páginas.
        """
        if isinstance(num_paginas, int) and num_paginas > 0:
            nueva_pagina = self.__pagina_actual + num_paginas
            if nueva_pagina <= self.__total_paginas:
                self.__pagina_actual = nueva_pagina
            else:
                raise ValueError(f"No se puede avanzar a la página {nueva_pagina}, excede el total de {self.__total_paginas} páginas.")
        else:
            raise ValueError("El número de páginas a avanzar debe ser un entero positivo.")

    def retroceder_pagina(self, num_paginas):
        """
        Retrocede un número de páginas en el libro.

        Args:
            num_paginas (int): El número de páginas a retroceder.

        Raises:
            ValueError: Si se intenta retroceder más allá de la página 1.
        """
        if isinstance(num_paginas, int) and num_paginas > 0:
            nueva_pagina = self.__pagina_actual - num_paginas
            if nueva_pagina >= 1:
                self.__pagina_actual = nueva_pagina
            else:
                raise ValueError("No se puede retroceder más allá de la página 1.")
        else:
            raise ValueError("El número de páginas a retroceder debe ser un entero positivo.")

    def obtener_pagina_actual(self):
        """
        Devuelve la página actual en la que se encuentra el lector.

        Returns:
            int: El número de la página actual.
        """
        return self.__pagina_actual

    def obtener_info_libro(self):
        """
        Devuelve la información completa del libro.

        Returns:
            str: Una cadena con el título, autor, número total de páginas y página actual.
        """
        return f"Título: {self.__titulo}, Autor: {self.__autor}, Total de páginas: {self.__total_paginas}, Página actual: {self.__pagina_actual}"

# Ejemplo de la clase Libro
if __name__ == "__main__":
    try:
        mi_libro = Libro("Cien años de soledad", "Gabriel García Márquez", 496)
        print(mi_libro.obtener_info_libro())
        print(f"Página actual: {mi_libro.obtener_pagina_actual()}")

        mi_libro.avanzar_pagina(50)
        print(f"Página actual después de avanzar: {mi_libro.obtener_pagina_actual()}")

        mi_libro.retroceder_pagina(25)
        print(f"Página actual después de retroceder: {mi_libro.obtener_pagina_actual()}")

        try:
            mi_libro.avanzar_pagina(500)
        except ValueError as e:
            print(f"Error al avanzar página: {e}")

        try:
            mi_libro.retroceder_pagina(30)
        except ValueError as e:
            print(f"Error al retroceder página: {e}")

        try:
            mi_libro.retroceder_pagina(mi_libro.obtener_pagina_actual())
        except ValueError as e:
            print(f"Error al retroceder página: {e}")

        otro_libro = Libro("El Principito", "Antoine de Saint-Exupéry", 96)
        otro_libro.avanzar_pagina(95)
        print(f"Página actual de '{otro_libro.obtener_info_libro().split(', ')[0].split(': ')[1]}': {otro_libro.obtener_pagina_actual()}")
        otro_libro.avanzar_pagina(1)
        print(f"Página actual de '{otro_libro.obtener_info_libro().split(', ')[0].split(': ')[1]}': {otro_libro.obtener_pagina_actual()}")
        try:
            otro_libro.avanzar_pagina(1)
        except ValueError as e:
            print(f"Error al avanzar página en '{otro_libro.obtener_info_libro().split(', ')[0].split(': ')[1]}': {e}")

    except ValueError as e:
        print(f"Error general: {e}")