class TarjetaCredito:
    """
    Clase para representar una tarjeta de crédito con un método estático
    para validar números de tarjeta utilizando el algoritmo de Luhn.
    """

    @staticmethod
    def validar_tarjeta(numero):
        """
        Método estático para validar un número de tarjeta de crédito
        utilizando el algoritmo de Luhn.

        Args:
            numero (str): El número de la tarjeta de crédito como una cadena.

        Returns:
            bool: True si el número de tarjeta es válido según el algoritmo de Luhn,
                  False en caso contrario.
        """
        numero = numero.replace(" ", "")  # Eliminar espacios
        if not numero.isdigit():
            return False

        n = len(numero)
        suma = 0
        alternar = False

        for i in range(n - 1, -1, -1):
            digito = int(numero[i])
            if alternar:
                digito *= 2
                if digito > 9:
                    digito -= 9
            suma += digito
            alternar = not alternar

        return (suma % 10 == 0)

# Ejemplo de la clase TarjetaCredito
if __name__ == "__main__":
    numero_valido = "49927398716"
    numero_invalido = "49927398717"
    numero_con_espacios = "4992 7398 716"
    numero_con_letras = "4992ABC8716"

    print(f"¿Es '{numero_valido}' una tarjeta válida? {TarjetaCredito.validar_tarjeta(numero_valido)}")
    print(f"¿Es '{numero_invalido}' una tarjeta válida? {TarjetaCredito.validar_tarjeta(numero_invalido)}")
    print(f"¿Es '{numero_con_espacios}' una tarjeta válida? {TarjetaCredito.validar_tarjeta(numero_con_espacios)}")
    print(f"¿Es '{numero_con_letras}' una tarjeta válida? {TarjetaCredito.validar_tarjeta(numero_con_letras)}")