import logging
from pathlib import Path


RUTA_LOGS = Path(__file__).resolve().parent.parent / "logs"

RUTA_LOGS.mkdir(parents=True, exist_ok=True)

RUTA_ARCHIVO = RUTA_LOGS / "eventos.log"

logger = logging.getLogger("SoftwareFJ")
logger.setLevel(logging.INFO)

if not logger.handlers:
    manejador = logging.FileHandler(
        RUTA_ARCHIVO,
        encoding="utf-8"
    )

    formato = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    manejador.setFormatter(formato)
    logger.addHandler(manejador)


def registrar_evento(mensaje):
    logger.info(mensaje)


def registrar_error(mensaje):
    logger.error(mensaje)