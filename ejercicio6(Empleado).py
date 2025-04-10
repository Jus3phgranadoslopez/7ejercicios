class Empleado:
    """
    Clase para representar a un empleado con nombre y salario,
    y llevar un registro del número total de empleados creados
    utilizando un método de clase.
    """
    contador_empleados = 0  # Atributo de clase para contar empleados

    def __init__(self, nombre, salario):
        """
        Constructor de la clase Empleado.

        Args:
            nombre (str): El nombre del empleado.
            salario (float): El salario del empleado.
        """
        self.nombre = nombre
        self.salario = salario
        Empleado.contador_empleados += 1  # Incrementa el contador al crear un empleado

    @classmethod
    def cantidad_empleados(cls):
        """
        Método de clase para obtener el número total de empleados creados.

        Returns:
            int: El número total de empleados.
        """
        return cls.contador_empleados

# Ejemplo de la clase Empleado
if __name__ == "__main__":
    print(f"Número inicial de empleados: {Empleado.cantidad_empleados()}")

    empleado1 = Empleado("Alice", 30000)
    print(f"Empleado creado: {empleado1.nombre}, Salario: ${empleado1.salario:.2f}")
    print(f"Número actual de empleados: {Empleado.cantidad_empleados()}")

    empleado2 = Empleado("Bob", 45000)
    print(f"Empleado creado: {empleado2.nombre}, Salario: ${empleado2.salario:.2f}")
    print(f"Número actual de empleados: {Empleado.cantidad_empleados()}")

    empleado3 = Empleado("Charlie", 35000)
    print(f"Empleado creado: {empleado3.nombre}, Salario: ${empleado3.salario:.2f}")
    print(f"Número total de empleados: {Empleado.cantidad_empleados()}")