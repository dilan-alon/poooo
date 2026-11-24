from abc import ABC, abstractmethod

class Pedido(ABC):
    def __init__(self, id_pedido, cliente, dia_semana):
        self._id_pedido = id_pedido
        self._cliente = cliente
        self._dia_semana = dia_semana
        self._productos = []
        self._estado = "REGISTRADO"

    @property
    def estado(self):
        return self._estado

    def cambiar_estado(self, nuevo_estado):
        transiciones_validas = {
            "REGISTRADO": ["EN_PREPARACION", "CANCELADO"],
            "EN_PREPARACION": ["LISTO"],
            "LISTO": ["ENTREGADO"]
        }
        if nuevo_estado not in transiciones_validas.get(self._estado, []):
            raise ValueError(f"Transición inválida de {self._estado} a {nuevo_estado}")
        self._estado = nuevo_estado

    def agregar_producto(self, producto):
        if self._estado != "REGISTRADO":
            raise ValueError("Solo se pueden agregar productos en estado REGISTRADO")
        if not producto.esta_disponible(self._dia_semana):
            raise ValueError(f"El producto {producto.nombre} no está disponible hoy.")
        self._productos.append(producto)

    @abstractmethod
    def calcular_cargos(self):
        pass

    def calcular_subtotal(self):
        return sum(p.calcular_precio() for p in self._productos)

    def calcular_total(self):
        return round(self.calcular_subtotal() + self.calcular_cargos(), 2)

    @abstractmethod
    def mostrar_detalle(self):
        pass

class PedidoLocal(Pedido):
    def __init__(self, id_pedido, cliente, dia_semana, numero_mesa):
        super().__init__(id_pedido, cliente, dia_semana)
        if not (1 <= numero_mesa <= 15):
            raise ValueError("La mesa debe ser entre 1 y 15")
        self._numero_mesa = numero_mesa

    def calcular_cargos(self):
        return 0.0 # Sin cargos adicionales

    def mostrar_detalle(self):
        return f"Pedido Local - Mesa {self._numero_mesa}"

class PedidoLlevar(Pedido):
    def calcular_cargos(self):
        # Variante A: Bs 2 por envase por cada plato (incluidos platos dentro de combos)
        total_platos = sum(p.contar_platos() for p in self._productos)
        return total_platos * 2.0

    def mostrar_detalle(self):
        return "Pedido Para Llevar"

class PedidoDelivery(Pedido):
    def __init__(self, id_pedido, cliente, dia_semana, zona):
        super().__init__(id_pedido, cliente, dia_semana)
        self._zona = zona
        self._costo_envio = 0.0

    def calcular_cargos(self):
        subtotal = self.calcular_subtotal()
        # Variante A: Pedido mínimo Bs 40
        if subtotal < 40:
            raise ValueError("El pedido mínimo para delivery es de Bs 40")

        tarifas = {"Cercado": 8, "Quillacollo": 15, "Sacaba": 15, "Vinto": 20}
        self._costo_envio = tarifas.get(self._zona, 0)

        # Variante A: Envío gratis en Cercado si subtotal >= 150
        if self._zona == "Cercado" and subtotal >= 150:
            self._costo_envio = 0.0
        
        return self._costo_envio

    def mostrar_detalle(self):
        return f"Delivery a {self._zona} (Envío: Bs {self._costo_envio})"