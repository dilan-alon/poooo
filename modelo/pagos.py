from abc import ABC, abstractmethod

class MetodoPago(ABC):
    def __init__(self):
        self._monto_pagado = 0.0

    @abstractmethod
    def procesar_pago(self, total):
        pass

class Efectivo(MetodoPago):
    def __init__(self, monto_recibido):
        super().__init__()
        self._monto_recibido = monto_recibido

    def procesar_pago(self, total):
        if self._monto_recibido < total:
            raise ValueError("El monto recibido no cubre el total")
        self._monto_pagado = total
        return self._monto_recibido - total

class Tarjeta(MetodoPago):
    def __init__(self, numero_tarjeta):
        super().__init__()
        self._numero_tarjeta = numero_tarjeta

    def procesar_pago(self, total):
        comision = total * 0.03
        self._monto_pagado = total + comision
        return 0.0

class PagoQR(MetodoPago):
    def __init__(self, codigo_transaccion):
        super().__init__()
        if len(str(codigo_transaccion)) != 10:
            raise ValueError("El código de transacción debe tener 10 dígitos")
        self._codigo_transaccion = codigo_transaccion

    def procesar_pago(self, total):
        self._monto_pagado = total
        return 0.0