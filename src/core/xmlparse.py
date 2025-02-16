# from time import sleep
import logging
from xml.dom import minidom

from .constants import (
    StrEnum
)


def create_list(file_name: str) -> list[str] | None:
    """Создание массива строк экрана"""
    logging.info("Создание массивa")
    try:
        nodes = minidom.parse(file_name).getElementsByTagName(StrEnum.NODE)
        return [
            x.getAttribute(
                StrEnum.TEXT
            ) for x in nodes if x.getAttribute(StrEnum.TEXT) != ''
            ]
    except Exception as error:
        logging.error(f"Не получилось создать массив строк, ошибка: {error}")
        return None
