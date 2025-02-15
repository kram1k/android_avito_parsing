# from time import sleep
import logging
from xml.dom import minidom

from .constants import (
    NODE,
    TEXT,
)


def create_list(file_name: str) -> list[str] | None:
    """Создание массива строк экрана"""
    logging.info("Создание массивa")
    try:
        nodes = minidom.parse(file_name).getElementsByTagName(NODE)
        return [
            x.getAttribute(TEXT) for x in nodes if x.getAttribute(TEXT) != ''
            ]
    except Exception as error:
        logging.error(f"Не получилось создать массив строк, ошибка: {error}")
        return None
