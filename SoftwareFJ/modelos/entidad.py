from abc import ABC, abstractmethod
from datetime import datetime
import uuid


class Entidad(ABC):

    def __init__(self):
        self.__id = str(uuid.uuid4())
        self.__fecha_creacion = datetime.now()

    @property
    def id(self):
        return self.__id

    @property
    def fecha_creacion(self):
        return self.__fecha_creacion

    @abstractmethod
    def obtener_descripcion(self):
        pass