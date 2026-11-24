from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, id_producto, nombre, precio_base):
        self._id_producto = id_producto
        self._nombre = nombre
        self._precio_base = precio_base

    @property
    def precio_base(self):
        return self._precio_base

    @property
    def nombre(self):
        return self._nombre

    @abstractmethod
    def calcular_precio(self):
        pass

    @abstractmethod
    def esta_disponible(self, dia_semana):
        pass

    @abstractmethod
    def contar_platos(self):
        pass

class Plato(Producto):
    def __init__(self, id_producto, nombre, precio_base, dias_disponibles):
        super().__init__(id_producto, nombre, precio_base)
        self._dias_disponibles = dias_disponibles

    def calcular_precio(self):
        return self.precio_base

    def esta_disponible(self, dia_semana):
        return dia_semana in self._dias_disponibles

    def contar_platos(self):
        return 1

class Bebida(Producto):
    def __init__(self, id_producto, nombre, precio_vaso, es_jarra=False):
        super().__init__(id_producto, nombre, precio_vaso)
        self._es_jarra = es_jarra

    def calcular_precio(self):
        if self._es_jarra:
            return self.precio_base * 3
        return self.precio_base

    def esta_disponible(self, dia_semana):
        return True

    def contar_platos(self):
        return 0

class Combo(Producto):
    def __init__(self, id_producto, nombre):
        super().__init__(id_producto, nombre, 0)
        self._productos = []

    def agregar_producto(self, producto):
        if len(self._productos) >= 4:
            raise ValueError("Un combo no puede tener más de 4 productos.")
        if producto == self:
            raise ValueError("Un combo no puede contenerse a sí mismo.")
        self._productos.append(producto)

    def calcular_precio(self):
        suma = sum(p.calcular_precio() for p in self._productos)
        return round(suma * 0.90, 2)

    def esta_disponible(self, dia_semana):
        for p in self._productos:
            if not p.esta_disponible(dia_semana):
                return False
        return True

    def contar_platos(self):
        return sum(p.contar_platos() for p in self._productos)