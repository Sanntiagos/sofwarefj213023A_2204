from modelos.cliente import Cliente
from modelos.reserva import Reserva

from servicios.sala import ServicioSala
from servicios.equipo import ServicioEquipo
from servicios.asesoria import ServicioAsesoria

from utilidades.logger import registrar_evento, registrar_error
from utilidades.excepciones import (
    ReservaError,
    OperacionNoPermitidaError
)


def ejecutar_sistema():

    print("=" * 60)
    print("       SISTEMA INTEGRAL DE GESTION - SOFTWARE FJ")
    print("=" * 60)

    # Listas internas del sistema
    clientes = []
    servicios = []
    reservas = []

    # OPERACION 1: Registrar cliente valido
    print("\nOPERACION 1: Registro de cliente")

    try:
        cliente = Cliente(
            "Carlos Perez",
            "12345678",
            "carlos@gmail.com",
            "3101234567"
        )

        clientes.append(cliente)

    except ValueError as error:
        registrar_error(f"Error registrando cliente: {error}")
        print("Error:", error)

    else:
        print("Cliente registrado correctamente.")
        print(cliente.obtener_descripcion())

    finally:
        print("Operacion de registro finalizada.")

    # OPERACION 2: Intentar registrar cliente invalido
    print("\nOPERACION 2: Registro de cliente invalido")

    try:
        cliente_invalido = Cliente(
            "AB",
            "123",
            "correo_invalido",
            "123"
        )

        clientes.append(cliente_invalido)

    except ValueError as error:
        registrar_error(f"Cliente invalido: {error}")
        print("Error controlado:", error)

    # OPERACION 3: Crear servicio de sala
    print("\nOPERACION 3: Crear servicio de sala")

    try:
        sala = ServicioSala(
            "Sala de reuniones",
            "Sala equipada para reuniones empresariales",
            50000,
            20
        )

        servicios.append(sala)
        print(sala.obtener_descripcion())

    except ValueError as error:
        registrar_error(str(error))
        print("Error:", error)

    # OPERACION 4: Crear servicio incorrecto
    print("\nOPERACION 4: Crear servicio invalido")

    try:
        servicio_invalido = ServicioSala(
            "Sala defectuosa",
            "Servicio de prueba",
            -5000,
            10
        )

        servicios.append(servicio_invalido)

    except ValueError as error:
        registrar_error(f"Servicio invalido: {error}")
        print("Error controlado:", error)

    # OPERACION 5: Crear servicio de alquiler de equipos
    print("\nOPERACION 5: Crear servicio de equipos")

    try:
        equipo = ServicioEquipo(
            "Computador portatil",
            "Alquiler de computador para trabajo",
            80000,
            10
        )

        servicios.append(equipo)
        print(equipo.obtener_descripcion())

    except ValueError as error:
        registrar_error(str(error))
        print("Error:", error)

    # OPERACION 6: Crear servicio de asesoria
    print("\nOPERACION 6: Crear servicio de asesoria")

    try:
        asesoria = ServicioAsesoria(
            "Asesoria de software",
            "Orientacion especializada en desarrollo",
            100000,
            "Ingeniero de sistemas"
        )

        servicios.append(asesoria)
        print(asesoria.obtener_descripcion())

    except ValueError as error:
        registrar_error(str(error))
        print("Error:", error)

    # OPERACION 7: Crear y confirmar una reserva
    print("\nOPERACION 7: Crear reserva")

    try:
        reserva1 = Reserva(cliente, sala, 2)

        reservas.append(reserva1)
        reserva1.confirmar()

        print("Reserva confirmada.")
        print(reserva1.obtener_descripcion())

    except (ValueError, OperacionNoPermitidaError) as error:
        registrar_error(str(error))
        print("Error:", error)

    # OPERACION 8: Procesar reserva correctamente
    print("\nOPERACION 8: Procesar reserva")

    try:
        costo = reserva1.procesar(
            impuesto=19,
            descuento=10
        )

        print(f"Costo total de la reserva: ${costo:,.2f}")

    except (ReservaError, OperacionNoPermitidaError) as error:
        registrar_error(str(error))
        print("Error:", error)

    # OPERACION 9: Intentar crear una reserva incorrecta
    print("\nOPERACION 9: Reserva con duracion invalida")

    try:
        reserva_invalida = Reserva(
            cliente,
            equipo,
            -3
        )

        reservas.append(reserva_invalida)

    except ValueError as error:
        registrar_error(f"Reserva invalida: {error}")
        print("Error controlado:", error)

    # OPERACION 10: Cancelar una reserva
    print("\nOPERACION 10: Cancelacion de reserva")

    try:
        reserva2 = Reserva(
            cliente,
            asesoria,
            2
        )

        reservas.append(reserva2)
        reserva2.confirmar()
        reserva2.cancelar()

        print("Reserva cancelada correctamente.")
        print(reserva2.obtener_descripcion())

    except (ValueError, OperacionNoPermitidaError) as error:
        registrar_error(str(error))
        print("Error:", error)

    # Resumen general
    print("\n" + "=" * 60)
    print("             RESUMEN DEL SISTEMA")
    print("=" * 60)

    print(f"Clientes registrados: {len(clientes)}")
    print(f"Servicios creados: {len(servicios)}")
    print(f"Reservas creadas: {len(reservas)}")

    print("\nESTADO DE LAS RESERVAS:")

    for reserva in reservas:
        print(reserva.obtener_descripcion())

    registrar_evento("Ejecucion del sistema finalizada.")

    print("\nLos eventos y errores se guardaron en logs/eventos.log")
    print("=" * 60)


if __name__ == "__main__":
    ejecutar_sistema()