from modelos.servicio import Servicio


class ServicioSala(Servicio):

    def __init__(self, nombre, descripcion, precio_base, capacidad):
        super().__init__(nombre, descripcion, precio_base)

        if not isinstance(capacidad, int) or isinstance(capacidad, bool) or capacidad <= 0:
            raise ValueError("La capacidad debe ser un entero positivo.")

        self.__capacidad = capacidad

    @property
    def capacidad(self):
        return self.__capacidad

    def validar_parametros(self, duracion):
        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or duracion <= 0
        ):
            raise ValueError("La duración debe ser mayor que cero.")

        return True

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_parametros(duracion)
        self.validar_porcentajes(impuesto, descuento)

        subtotal = self.precio_base * duracion
        subtotal -= subtotal * (descuento / 100)
        total = subtotal + subtotal * (impuesto / 100)

        return round(total, 2)

    def obtener_descripcion(self):
        return (
            f"Sala: {self.nombre} | "
            f"Capacidad: {self.capacidad} personas | "
            f"Precio por hora: ${self.precio_base:,.2f}"
        )