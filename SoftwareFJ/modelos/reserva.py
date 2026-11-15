from modelos.entidad import Entidad
from utilidades.excepciones import ReservaError, OperacionNoPermitidaError
from utilidades.logger import registrar_evento, registrar_error


class Reserva(Entidad):

    def __init__(self, cliente, servicio, duracion):
        super().__init__()

        if cliente is None:
            raise ValueError("Debe existir un cliente.")

        if servicio is None:
            raise ValueError("Debe existir un servicio.")

        servicio.validar_parametros(duracion)

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "PENDIENTE"
        self.__costo = None

        registrar_evento(f"Reserva creada: {self.id}")

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    @property
    def costo(self):
        return self.__costo

    def confirmar(self):
        if self.__estado != "PENDIENTE":
            raise OperacionNoPermitidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        self.__estado = "CONFIRMADA"
        registrar_evento(f"Reserva confirmada: {self.id}")

    def cancelar(self):
        if self.__estado not in ("PENDIENTE", "CONFIRMADA"):
            raise OperacionNoPermitidaError(
                "La reserva no se puede cancelar."
            )

        self.__estado = "CANCELADA"
        registrar_evento(f"Reserva cancelada: {self.id}")

    def procesar(self, impuesto=0, descuento=0):
        if self.__estado != "CONFIRMADA":
            raise OperacionNoPermitidaError(
                "La reserva debe estar confirmada."
            )

        try:
            self.__costo = self.__servicio.calcular_costo(
                self.__duracion, impuesto, descuento
            )

            self.__estado = "PROCESADA"
            registrar_evento(
                f"Reserva procesada: {self.id}. "
                f"Costo: ${self.__costo:,.2f}"
            )

            return self.__costo

        except Exception as error:
            registrar_error(f"Error procesando reserva {self.id}: {error}")

            raise ReservaError(
                "No fue posible procesar la reserva."
            ) from error

    def obtener_descripcion(self):
        return (
            f"Reserva: {self.id} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Estado: {self.estado}"
        )