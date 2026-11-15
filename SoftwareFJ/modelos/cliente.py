import re
from modelos.entidad import Entidad


class Cliente(Entidad):

    def __init__(self, nombre, documento, correo, telefono):
        super().__init__()

        self.__nombre = self.validar_nombre(nombre)
        self.__documento = self.validar_documento(documento)
        self.__correo = self.validar_correo(correo)
        self.__telefono = self.validar_telefono(telefono)

    def validar_nombre(self, nombre):
        if not isinstance(nombre, str) or len(nombre.strip()) < 3:
            raise ValueError("El nombre debe tener mínimo 3 caracteres.")
        return nombre.strip()

    def validar_documento(self, documento):
        documento = str(documento).strip()

        if not documento.isdigit() or len(documento) < 5:
            raise ValueError("Documento inválido.")

        return documento

    def validar_correo(self, correo):
        if not isinstance(correo, str):
            raise ValueError("El correo debe ser texto.")

        patron = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"

        if not re.match(patron, correo.strip()):
            raise ValueError("Correo electrónico inválido.")

        return correo.strip().lower()

    def validar_telefono(self, telefono):
        telefono = str(telefono).strip()

        if not telefono.isdigit() or not 7 <= len(telefono) <= 15:
            raise ValueError("Teléfono inválido.")

        return telefono

    @property
    def nombre(self):
        return self.__nombre

    @property
    def documento(self):
        return self.__documento

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def obtener_descripcion(self):
        return (
            f"Cliente: {self.nombre} | "
            f"Documento: {self.documento} | "
            f"Correo: {self.correo} | "
            f"Teléfono: {self.telefono}"
        )