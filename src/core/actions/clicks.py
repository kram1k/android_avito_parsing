import logging

from uiautomator2 import Device, UiObject

from ..constants import FloatEnum, StrEnum, XmlClassEnum, XmlIdEnum, XpathEnum

logger_activities = logging.getLogger(__name__)


def click_search_list_item(device: Device, query: str) -> UiObject:
    """Получение элемента из поисковой выдачи"""

    logging.info(click_search_list_item.__doc__)
    try:
        return device(
            text=query,
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
    """Подтверждение изменений в фильтре поиска"""
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


def click_paste_url_in_input(device: Device):
    """Нажатие на кнопку 'Вставить'"""
    logging.info(click_paste_url_in_input.__doc__)
    try:
        return device.xpath(XpathEnum.PASTE).click()
    except Exception as error:
        logging.error(f"Не удалось вставить URL, ошибка {error}")


def click_select_all_url(device: Device):
    """Нажатие на кнопку 'Выделит все'"""
    logging.info(click_select_all_url.__doc__)
    try:
        return device.xpath(XpathEnum.SELECT_ALL).click()
    except Exception as error:
        logging.error(f"Не удалось выделить весть текст, ошибка {error}")


def click_delete_url_in_input(device: Device):
    """Удаление URL из виджета ''Измение текста'"""
    logging.info(click_delete_url_in_input.__doc__)
    try:
        return device.xpath(XpathEnum.KEY_POS_DEL).click()
    except Exception as error:
        logging.error(f"Не удалось удалить URL, ошибка {error}")


def click_to_announcement(device: Device, idx: int):
    """Нажатие на обьвление"""
    logging.info(click_to_announcement.__doc__)
    try:
        return device(
            index=str(idx),
            resourceId=XmlIdEnum.ADVERT_GRID_ROOT,
            className=XmlClassEnum.FRAME_LAYOUT).click()
    except Exception as error:
        logging.error(
            f"Не удалось нажать на обьявление {idx + 1}, ошибка {error}"
        )


def click_share_button(device: Device) -> UiObject:
    """Нажатие на кнопку 'Поделится'"""
    logging.info(click_share_button.__doc__)
    try:
        return device(
            resourceId=XmlIdEnum.MENU_SHARE,
            className=XmlClassEnum.BUTTON,
        ).click()
    except Exception as error:
        logging.error(f"Не удалось найти кнопку 'Поделится', ошибка: {error}")


def click_copy_button(device: Device) -> UiObject:
    """Нажатие на кнопку 'Копировать'"""
    logging.info(click_copy_button.__doc__)
    try:
        return device(
            text=StrEnum.COPY_BUTTON,
            resourceId=XmlIdEnum.TEXT1,
            className=XmlClassEnum.TEXT_VIEW,
        ).click()
    except Exception as error:
        logging.error(f"Не удалось найти кнопку 'Копировать', ошибка: {error}")
