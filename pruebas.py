from modelo.productos import Plato, Bebida, Combo
from modelo.pedidos import PedidoDelivery
from modelo.clientes import Cliente

def ejecutar_pruebas():
    print("Ejecutando pruebas...")
    
    try:
        Cliente(1, "Juan", "12345678")
        assert False
    except ValueError:
        pass

    silpancho = Plato(1, "Silpancho", 35.0, ["Lunes", "Martes"])
    mocochinchi = Bebida(2, "Mocochinchi", 6.0)
    combo = Combo(3, "Combo Sabor")
    combo.agregar_producto(silpancho)
    combo.agregar_producto(mocochinchi)
    
    assert combo.calcular_precio() == 36.90

    cliente = Cliente(1, "Maria", "71234567")
    pedido = PedidoDelivery(1, cliente, "Lunes", "Quillacollo")
    pedido.agregar_producto(combo)
    pedido.agregar_producto(combo)
    
    assert pedido.calcular_total() == 88.80

    try:
        pedido.cambiar_estado("ENTREGADO")
        assert False
    except ValueError:
        pass

    super_combo = Combo(4, "Mega Combo")
    super_combo.agregar_producto(combo)
    assert super_combo.calcular_precio() == 33.21

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    ejecutar_pruebas()