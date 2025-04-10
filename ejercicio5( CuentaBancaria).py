class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        """
        Constructor de la clase CuentaBancaria.

        Args:
            titular (str): El nombre del titular de la cuenta.
            saldo_inicial (float): El saldo inicial de la cuenta (por defecto 0).

        Raises:
            ValueError: Si el saldo inicial es negativo.
        """
        self._titular = titular  # Atributo protegido
        if saldo_inicial >= 0:
            self._saldo = saldo_inicial  # Atributo protegido
        else:
            raise ValueError("El saldo inicial no puede ser negativo.")

    def depositar(self, cantidad):
        """
        Deposita una cantidad en la cuenta.

        Args:
            cantidad (float): La cantidad a depositar.

        Raises:
            ValueError: Si la cantidad a depositar no es positiva.
        """
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Se depositaron ${cantidad:.2f} en la cuenta de {self._titular}. Saldo actual: ${self._saldo:.2f}")
        else:
            raise ValueError("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        """
        Retira una cantidad de la cuenta.

        Args:
            cantidad (float): La cantidad a retirar.

        Raises:
            ValueError: Si la cantidad a retirar no es positiva o si excede el saldo actual.
        """
        if cantidad > 0:
            if cantidad <= self._saldo:
                self._saldo -= cantidad
                print(f"Se retiraron ${cantidad:.2f} de la cuenta de {self._titular}. Saldo actual: ${self._saldo:.2f}")
            else:
                raise ValueError("Saldo insuficiente.")
        else:
            raise ValueError("La cantidad a retirar debe ser positiva.")

    def consultar_saldo(self):
        """
        Consulta el saldo actual de la cuenta.

        Returns:
            float: El saldo actual.
        """
        return self._saldo

    def obtener_titular(self):
        """
        Obtiene el nombre del titular de la cuenta.

        Returns:
            str: El nombre del titular.
        """
        return self._titular

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo_inicial=0, porcentaje_interes_anual=0):
        """
        Constructor de la clase CuentaAhorro, que hereda de CuentaBancaria.

        Args:
            titular (str): El nombre del titular de la cuenta.
            saldo_inicial (float): El saldo inicial de la cuenta (por defecto 0).
            porcentaje_interes_anual (float): El porcentaje de interés anual (por defecto 0).

        Raises:
            ValueError: Si el porcentaje de interés anual es negativo.
        """
        super().__init__(titular, saldo_inicial)
        if porcentaje_interes_anual >= 0:
            self.__porcentaje_interes_anual = porcentaje_interes_anual / 100  # Almacenar como decimal
        else:
            raise ValueError("El porcentaje de interés anual no puede ser negativo.")

    def aplicar_interes(self):
        """
        Aplica el interés anual al saldo actual de la cuenta.
        """
        interes = self._saldo * self.__porcentaje_interes_anual
        self._saldo += interes
        print(f"Se aplicó un interés de ${interes:.2f} a la cuenta de ahorro de {self._titular}. Nuevo saldo: ${self._saldo:.2f}")

    def consultar_interes(self):
        """
        Consulta el porcentaje de interés anual actual de la cuenta.

        Returns:
            float: El porcentaje de interés anual actual.
        """
        return self.__porcentaje_interes_anual * 100

# Ejemplo de las clases
if __name__ == "__main__":
    try:
        cuenta_corriente = CuentaBancaria("Juan Pérez", 1000)
        print(f"Titular: {cuenta_corriente.obtener_titular()}, Saldo: ${cuenta_corriente.consultar_saldo():.2f}")
        cuenta_corriente.depositar(500)
        cuenta_corriente.retirar(200)

        cuenta_ahorro = CuentaAhorro("María Gómez", 5000, 3)
        print(f"\nTitular (Ahorro): {cuenta_ahorro.obtener_titular()}, Saldo: ${cuenta_ahorro.consultar_saldo():.2f}, Interés anual: {cuenta_ahorro.consultar_interes():.2f}%")
        cuenta_ahorro.depositar(1000)
        cuenta_ahorro.aplicar_interes()
        cuenta_ahorro.retirar(1500)
        cuenta_ahorro.aplicar_interes()

        try:
            cuenta_negativa = CuentaBancaria("Pedro López", -100)
        except ValueError as e:
            print(f"\nError al crear cuenta corriente: {e}")

        try:
            cuenta_interes_negativo = CuentaAhorro("Ana Vargas", 2000, -1)
        except ValueError as e:
            print(f"Error al crear cuenta de ahorro: {e}")

    except ValueError as e:
        print(f"Error general: {e}")