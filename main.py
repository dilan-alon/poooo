from restaurante import Restaurante
from modelo.productos import Plato, Bebida

def main():
    print("--- Sistema Sabor Valluno ---")
    resto = Restaurante()
    
    chicharron = Plato(1, "Chicharrón", 30.0, ["Domingo"])
    silpancho = Plato(2, "Silpancho", 35.0, ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"])
    
    resto.registrar_producto(chicharron)
    resto.registrar_producto(silpancho)
    
    resto.listar_menu("Lunes")
    resto.listar_menu("Domingo")

if __name__ == "__main__":
    main()