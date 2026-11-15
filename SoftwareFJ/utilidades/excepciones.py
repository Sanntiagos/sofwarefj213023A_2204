class SoftwareFJError(Exception):
    """Excepción general del sistema Software FJ."""
    pass


class ClienteError(SoftwareFJError):
    pass


class ServicioError(SoftwareFJError):
    pass


class ReservaError(SoftwareFJError):
    pass


class OperacionNoPermitidaError(SoftwareFJError):
    pass


class ServicioNoDisponibleError(SoftwareFJError):
    pass