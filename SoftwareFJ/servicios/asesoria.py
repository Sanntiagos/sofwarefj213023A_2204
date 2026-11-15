from modelos.servicio import Servicio


class ServicioAsesoria(Servicio):

    def __init__(self, nombre, descripcion, precio_base, especialista):
        super().__init__(nombre, descripcion, precio_base)

        if not isinstance(especialista, str) or len(especialista.strip()) < 3:
            raise ValueError("Debe indicar un especialista válido.")

        self.__especialista = especialista.strip()

    @property
    def especialista(self):
        return self.__especialista

    def validar_parametros(self, duracion):
        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or duracion <= 0
        ):
            raise ValueError("Las horas de asesoría deben ser mayores que cero.")

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
            f"Asesoría: {self.nombre} | "
            f"Especialista: {self.especialista} | "
            f"Precio por hora: ${self.precio_base:,.2f}"
        )