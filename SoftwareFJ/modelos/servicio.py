from abc import abstractmethod
from modelos.entidad import Entidad


class Servicio(Entidad):

    def __init__(self, nombre, descripcion, precio_base):
        super().__init__()

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del servicio es obligatorio.")

        if not isinstance(descripcion, str) or not descripcion.strip():
            raise ValueError("La descripción es obligatoria.")

        if (
            not isinstance(precio_base, (int, float))
            or isinstance(precio_base, bool)
            or precio_base <= 0
        ):
            raise ValueError("El precio debe ser mayor que cero.")

        self.__nombre = nombre.strip()
        self.__descripcion = descripcion.strip()
        self.__precio_base = float(precio_base)

    @property
    def nombre(self):
        return self.__nombre

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def precio_base(self):
        return self.__precio_base

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def validar_parametros(self, duracion):
        pass

    @abstractmethod
    def obtener_descripcion(self):
        pass

    def validar_porcentajes(self, impuesto, descuento):
        if not 0 <= impuesto <= 100:
            raise ValueError("El impuesto debe estar entre 0 y 100.")

        if not 0 <= descuento <= 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")