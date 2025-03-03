from time import sleep
import logging

from uiautomator2 import Device

from .constants import (
    StrEnum,
)

logger_activities = logging.getLogger(__name__)


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
