class Cliente:
    def __init__(self, id_cliente, nombre, telefono):
        self._id_cliente = id_cliente
        self._nombre = nombre
        self._telefono = telefono
        
        if len(str(telefono)) != 8 or str(telefono)[0] not in ['6', '7']:
            raise ValueError("El teléfono debe tener 8 dígitos y empezar con 6 o 7")

    @property
    def nombre(self):
        return self._nombre