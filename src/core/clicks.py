import logging

from uiautomator2 import Device, UiObject

from .constants import (
    StrEnum, XmlIdEnum,
    XmlClassEnum, FloatEnum,
    XpathEnum
)

logger_activities = logging.getLogger(__name__)


def click_search_list_item(device: Device) -> UiObject:
    """Получение элемента из поисковой выдачи"""

    logging.info(click_search_list_item.__doc__)
    try:
        return device(
            text=StrEnum.SEARCH_TEXT,
            resourceId=XmlIdEnum.SUGGEST_TITLE,
            className=XmlClassEnum.TEXT_VIEW,
        ).click()
    except Exception as error:
        logging.error(f"Не удалось найти элемент, ошибка {error}")


def click_button_filter(device: Device) -> UiObject:
    """Получение кнопки для настройки фильтрации"""
    logging.info(click_button_filter.__doc__)
    try:
        return device(
            text=StrEnum.FILTER_BUTTON,
            className=XmlClassEnum.TEXT_VIEW,
            resourceId=XmlIdEnum.FILTERS_TEXT,
        ).click()
    except Exception as error:
        logging.error(f"Не удалось найти кнопку, ошибка {error}")


def click_toggle_date_button(device: Device) -> UiObject:
    """Измение сортировки на режим 'По дате'"""
    logging.info(click_toggle_date_button.__doc__)
    try:
        return device(
            resourceId=XmlIdEnum.FILTERS_SCREEN_ROOT,
            className=XmlClassEnum.FRAME_LAYOUT) \
            .child_by_text(
                txt=StrEnum.TO_DATE,
                resourceId=XmlIdEnum.DESIGN_ITEM_TITLE,
                allow_scroll_search=True,
                className=XmlClassEnum.TEXT_VIEW,
            ).click()
    except Exception as error:
        logging.error(
            f"Не удалось найти кнопку-переключатель {StrEnum.TO_DATE}",
            f" ошибка {error}"
        )


def click_accept_button(device: Device) -> UiObject:
    """Подтверждение изменений в филтре поиска"""
    logging.info(click_accept_button.__doc__)
    try:
        return device(
                text=StrEnum.ACCEPT_BUTTON,
                resourceId=XmlIdEnum.TEXT_VIEW,
                className=XmlClassEnum.TEXT_VIEW,
            ).click()

    except Exception as error:
        logging.error(f"Не удалось найти кнопку: {error}")


def long_click_to_edit_text(device: Device):
    """Длинное нажатие на виджет 'Измение текста'"""
    logging.info(long_click_to_edit_text.__doc__)
    try:
        return device(
            className=XmlClassEnum.EDIT_TEXT
        ).long_click(duration=FloatEnum.DURACTION_LONG_CLICK)
    except Exception as error:
        logging.error(f"Не удалось нажать на 'Измение текста', ошибка {error}")


def click_paste_url_in_input(device: Device) -> None:
    """Нажатие на кнопку 'Вставить'"""
    logging.info(click_paste_url_in_input.__doc__)
    try:
        return device.xpath(XpathEnum.PASTE).click()
    except Exception as error:
        logging.error(f"Не удалось вставить URL, ошибка {error}")


def click_select_all_url(device: Device) -> None:
    """Нажатие на кнопку 'Выделит все'"""
    logging.info(click_select_all_url.__doc__)
    try:
        return device.xpath(XpathEnum.SELECT_ALL).click()
    except Exception as error:
        logging.error(f"Не удалось выделить весть текст, ошибка {error}")


def click_delete_url_in_input(device: Device) -> None:
    """Удаление URL из виджета ''Измение текста'"""
    logging.info(click_delete_url_in_input.__doc__)
    try:
        return device.xpath(XpathEnum.KEY_POS_DEL).click()
    except Exception as error:
        logging.error(f"Не удалось удалить URL, ошибка {error}")
