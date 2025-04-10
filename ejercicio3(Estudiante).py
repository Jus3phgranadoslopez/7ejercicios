class Estudiante:
    def __init__(self, nombre, edad):
        """
        Constructor de la clase Estudiante.

        Args:
            nombre (str): El nombre del estudiante.
            edad (int): La edad del estudiante.

        Raises:
            ValueError: Si la edad no es un entero positivo.
        """
        self.__nombre = nombre  # Atributo privado
        if isinstance(edad, int) and edad > 0:
            self.__edad = edad  # Atributo privado
        else:
            raise ValueError("La edad del estudiante debe ser un entero positivo.")
        self.__notas = []  # Atributo privado: lista para almacenar las notas

    def agregar_nota(self, nota):
        """
        Agrega una nueva nota a la lista de notas del estudiante.

        Args:
            nota (float): La nota a agregar (debe estar entre 0 y 100).

        Raises:
            ValueError: Si la nota no está en el rango de 0 a 100.
        """
        if 0 <= nota <= 100:
            self.__notas.append(nota)
        else:
            raise ValueError("La nota debe estar en el rango de 0 a 100.")

    def calcular_promedio(self):
        """
        Calcula y devuelve el promedio de las notas del estudiante.

        Returns:
            float: El promedio de las notas. Devuelve 0 si no hay notas.
        """
        if self.__notas:
            return sum(self.__notas) / len(self.__notas)
        else:
            return 0

    def obtener_nombre(self):
        """
        Devuelve el nombre del estudiante.

        Returns:
            str: El nombre del estudiante.
        """
        return self.__nombre

    def obtener_edad(self):
        """
        Devuelve la edad del estudiante.

        Returns:
            int: La edad del estudiante.
        """
        return self.__edad

# Ejemplo de la clase Estudiante
if __name__ == "__main__":
    try:
        estudiante1 = Estudiante("Ana Pérez", 20)
        print(f"Nombre: {estudiante1.obtener_nombre()}, Edad: {estudiante1.obtener_edad()}")

        estudiante1.agregar_nota(85)
        estudiante1.agregar_nota(92)
        estudiante1.agregar_nota(78)
        print(f"Promedio de notas: {estudiante1.calcular_promedio():.2f}")

        try:
            estudiante1.agregar_nota(105)
        except ValueError as e:
            print(f"Error al agregar nota: {e}")

        estudiante2 = Estudiante("Carlos López", 19)
        print(f"Nombre: {estudiante2.obtener_nombre()}, Edad: {estudiante2.obtener_edad()}")
        print(f"Promedio de notas de {estudiante2.obtener_nombre()}: {estudiante2.calcular_promedio():.2f} (sin notas)")

        try:
            estudiante3 = Estudiante("Sofía Gómez", -5)
        except ValueError as e:
            print(f"Error al crear estudiante: {e}")

    except ValueError as e:
        print(f"Error general: {e}")