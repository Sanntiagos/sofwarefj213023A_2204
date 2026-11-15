from modelos.servicio import Servicio


class ServicioEquipo(Servicio):

    def __init__(self, nombre, descripcion, precio_base, cantidad):
        super().__init__(nombre, descripcion, precio_base)

        if not isinstance(cantidad, int) or isinstance(cantidad, bool) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero positivo.")

        self.__cantidad = cantidad

    @property
    def cantidad(self):
        return self.__cantidad

    def validar_parametros(self, duracion):
        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or duracion <= 0
        ):
            raise ValueError("Los días de alquiler deben ser mayores que cero.")

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
            f"Equipo: {self.nombre} | "
            f"Cantidad disponible: {self.cantidad} | "
            f"Precio por día: ${self.precio_base:,.2f}"
        )