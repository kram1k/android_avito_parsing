import logging
from time import sleep

from uiautomator2 import Device, Direction, UiObject

from ..constants import IntEnum, StrEnum, XmlClassEnum, XmlIdEnum

logger_activities = logging.getLogger(__name__)

UniqueId = int
TimePublish = str
Advertisements = tuple[UniqueId, TimePublish]


def get_button_container(device: Device) -> UiObject:
    """Получение кнопки input для поиска"""
    logging.info(get_button_container.__doc__)
    try:
        return device(
            text=StrEnum.RU_SEARCH_TEXT,
            resourceId="",
            className=XmlClassEnum.EDIT_TEXT,
        )
    except Exception as error:
        logging.error(f"Не удалось найти поле, ошибка {error}")


def get_new_item(device: Device, text: str) -> UiObject:
    """Получение нового объекта"""
    logging.info(get_new_item.__doc__)
    try:
        return device(
            resourceId=XmlIdEnum.MAIN_TEXT,
            className=XmlClassEnum.TEXT_VIEW,
            text=text,
        )
    except Exception as error:
        logging.error(f"Не удалось найти новый объект, ошибка: {error}")


def get_url_from_app_url(device: Device) -> str | None:
    """Получение URL из виджета 'Измение текста'"""
    logging.info(get_url_from_app_url.__doc__)
    try:
        return device(
            className=XmlClassEnum.EDIT_TEXT
        ).info[StrEnum.DEVICE_INFO_TEXT]
    except Exception as error:
        logging.error(f"Не удалось копировать URL, ошибка {error}")
        return None


def get_info_about_ad(device: Device) -> Advertisements:
    for _ in range(IntEnum.COUNT_SCROLLS):
        device(
            resourceId=XmlIdEnum.ADVERT_DETAILS_CONTAINER,
            className=XmlClassEnum.FRAME_LAYOUT,
        ).swipe(direction=Direction.UP, steps=IntEnum.SWIPE_STEP)
    sleep(IntEnum.WAIT_END_OPERTION)
    advert_number = device(
        className=XmlClassEnum.TEXT_VIEW,
        resourceId=XmlIdEnum.ADVERT_NUMBER
    ).info[StrEnum.TEXT].split()
    device.press(StrEnum.BACK)
    return (UniqueId(advert_number[1][1:]),
            advert_number[-1])
