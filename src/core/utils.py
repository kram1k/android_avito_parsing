from time import sleep
import logging
import re
from xml.dom import minidom

from uiautomator2 import Device

from .activities import write_xml, swipe_screen
from .constants import (
    StrEnum,
    FloatEnum
)


def create_list(file_name: str) -> list[str] | None:
    """Создание массива строк экрана"""
    logging.info("Создание массивa")
    try:
        nodes = minidom.parse(file_name).getElementsByTagName(StrEnum.NODE)
        array = []
        for chars in nodes:
            text = chars.getAttribute(StrEnum.TEXT)
            positions = re.search(StrEnum.TARGET, text).span()
            if positions != (0, 0) and text != '':
                array.append(text)
        return array
    except Exception as error:
        logging.error(f"Не получилось создать массив строк, ошибка: {error}")
        return None


def append_link_to_file(link: str) -> None:
    with open(StrEnum.RESULT_TXT, "w", encoding=StrEnum.UTF) as f:
        f.write(f"{link}\n")


def fill_lists(device: Device) -> tuple[list[str] | None, list[str] | None]:
    write_xml(device, StrEnum.FIRST_SCREEN)
    first_screen = create_list(StrEnum.FIRST_SCREEN)
    sleep(FloatEnum.DELAY_SCREEN)
    swipe_screen(device)
    write_xml(device, StrEnum.SECOND_SCREEN)
    second_screen = create_list(StrEnum.SECOND_SCREEN)
    return first_screen, second_screen
