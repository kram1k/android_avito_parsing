from time import sleep
import logging
import re
from xml.dom import minidom

from uiautomator2 import Device, UiObject

from .activities import swipe_screen
from .constants import (
    StrEnum, XmlIdEnum,
    XmlClassEnum
)

logger_activities = logging.getLogger(__name__)


def create_list(file_name: str) -> list[str] | None:
    """Создание массива строк экрана"""
    logging.info("Создание массивa")
    try:
        nodes = minidom.parse(file_name).getElementsByTagName(StrEnum.NODE)
        array = []
        for chars in nodes:
            text = chars.getAttribute(StrEnum.TEXT)
            if re.search(StrEnum.TARGET, text).span() != (0, 0) and text != '':
                array.append(text)
        return array
    except Exception as error:
        logging.error(f"Не получилось создать массив строк, ошибка: {error}")
        return None


def append_link_to_file(link: str) -> None:
    """Добавление ссылки в файл"""
    sleep(2)
    with open(StrEnum.RESULT_TXT, "w", encoding=StrEnum.UTF) as f:
        f.write(f"{link}\n")


def write_xml(device: Device, xml_file: str = StrEnum.DEV_XML_FILE) -> None:
    """Запись виджетов экрана в формате xml в файл"""
    logging.info(f"{write_xml.__doc__}: {xml_file}")
    try:
        with open(xml_file, "w", encoding=StrEnum.UTF) as f:
            f.write(device.dump_hierarchy())
            f.close
    except Exception as error:
        logging.error(
            f"Не удалось записать dump в файл {xml_file}, ошибка {error}"
        )
