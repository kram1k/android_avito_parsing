import logging

from uiautomator2 import Device, UiObject

from .constants import (
    StrEnum, XmlIdEnum,
    XmlClassEnum
)

logger_activities = logging.getLogger(__name__)


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


def get_share_button(device: Device) -> UiObject:
    """Получение кнопки 'Поделится'"""
    logging.info(get_share_button.__doc__)
    try:
        return device(
            resourceId=XmlIdEnum.MENU_SHARE,
            className=XmlClassEnum.BUTTON,
        )
    except Exception as error:
        logging.error(f"Не удалось найти кнопку 'Поделится', ошибка: {error}")


def get_note_button(device: Device) -> UiObject:
    """Получение кнопки 'Копировать'"""
    logging.info(get_note_button.__doc__)
    try:
        return device(
            text=StrEnum.COPY_BUTTON,
            resourceId=XmlIdEnum.TEXT1,
            className=XmlClassEnum.TEXT_VIEW,
        )
    except Exception as error:
        logging.error(f"Не удалось найти кнопку 'Копировать', ошибка: {error}")


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
