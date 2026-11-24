class Restaurante:
    def __init__(self):
        self._menu = []
        self._clientes = []
        self._pedidos = []

    def registrar_producto(self, producto):
        self._menu.append(producto)

    def registrar_cliente(self, cliente):
        self._clientes.append(cliente)

    def registrar_pedido(self, pedido):
        self._pedidos.append(pedido)

    def listar_menu(self, dia):
        print(f"\n--- Menú del {dia} ---")
        for p in self._menu:
            if p.esta_disponible(dia):
                print(f"{p.nombre} - Bs {p.calcular_precio()}")

    def reporte_ventas(self):
        print("\n--- Reporte de Ventas ---")
        pass