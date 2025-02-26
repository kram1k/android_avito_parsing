import logging
from time import sleep

from uiautomator2 import Device, UiObject, Direction

from .constants import StrEnum, IntEnum, XmlIdEnum, XmlClassEnum

logger_activities = logging.getLogger(__name__)


def write_xml(device: Device, xml_file: str) -> None:
    """Запись элементов экрана в формате xml в файл"""

    logging.info(f"Запись файла {xml_file}")
    try:
        with open(xml_file, "w", encoding=StrEnum.UTF) as f:
            f.write(device.dump_hierarchy())
            f.close
    except Exception as error:
        logging.error(
            f"Не удалось записать dump в файл {xml_file}, ошибка {error}"
        )


def get_button_container(device: Device) -> UiObject:
    """Получение кнопки input для поиска"""

    logging.info("Поиск кнопки поиска")
    try:
        return device(
            text=StrEnum.RU_SEARCH_TEXT,
            resourceId="",
            className=XmlClassEnum.EDIT_TEXT
        )
    except Exception as error:
        logging.error(f"Не удалось найти поле, ошибка {error}")


def get_search_list_item(device: Device) -> UiObject:
    """Получение элемента из поисковой выдачи"""

    logging.info("Поиск элемента в поисковой выдачи")
    try:
        return device(
            text=StrEnum.SEARCH_TEXT,
            resourceId=XmlIdEnum.SUGGEST_TITLE,
            className=XmlClassEnum.TEXT_VIEW
        )
    except Exception as error:
        logging.error(f"Не удалось найти элемент, ошибка {error}")


def get_button_filter(device: Device) -> UiObject:
    """Получение кнопки для настройки фильтрации"""

    logging.info("Поиск кнопки фильтра")
    try:
        return device(
            text=StrEnum.FILTER_BUTTON,
            className=XmlClassEnum.TEXT_VIEW,
            resourceId=XmlIdEnum.FILTERS_TEXT
        )
    except Exception as error:
        logging.error(f"Не удалось найти кнопку, ошибка {error}")


def get_cords_swipe_down(device: Device) -> None:
    """Прокрутка экрана до нужного компонента"""
    logging.info("Начало оперции прокрутки...")
    for _ in range(IntEnum.COUNT_SCROLLS):
        device(
            resourceId=XmlIdEnum.CONTENT,
            className=XmlClassEnum.FRAME_LAYOUT) \
            .swipe(direction=Direction.UP, steps=IntEnum.TIME_TO_SCROLL)
    logging.info("Ожидание ее окончания")
    sleep(IntEnum.WAIT_SCROLL_DONE)


def get_toggle_date_button(device: Device) -> UiObject:
    """Измение сортировки на режим 'По дате'"""
    logging.info(f"Поиск кнопки для фильтрации: {StrEnum.TO_DATE}")
    try:
        return device(
            resourceId=XmlIdEnum.FILTERS_SCREEN_ROOT,
            className=XmlClassEnum.FRAME_LAYOUT) \
            .child_by_text(
                txt=StrEnum.TO_DATE,
                resourceId=XmlIdEnum.DESIGN_ITEM_TITLE,
                allow_scroll_search=True,
                className=XmlClassEnum.TEXT_VIEW
            )
    except Exception as error:
        logging.error(
            f"Не удалось найти кнопку-переключатель {StrEnum.TO_DATE}",
            f" ошибка {error}"
        )


def get_accept_button(device: Device) -> UiObject:
    """Подтверждение изменений в филтре поиска"""
    logging.info("Поиск кнопки подтверждения изменений")
    try:
        return device(
                text=StrEnum.ACCEPT_BUTTON,
                resourceId=XmlIdEnum.TEXT_VIEW,
                className=XmlClassEnum.TEXT_VIEW
            )

    except Exception as error:
        logging.error(f"Не удалось найти кнопку: {error}")


def swipe_screen(device: Device):
    device().swipe(direction=Direction.DOWN)


def get_new_item(device: Device, text: str) -> UiObject:
    """Получение нового объекта"""
    logging.info("Поиск нового объекта")
    try:
        return device(
            resourceId=XmlIdEnum.MAIN_TEXT,
            className=XmlClassEnum.TEXT_VIEW,
            text=text
        )    
    except Exception as error:
        logging.error(f"Не удалось найти новый объект, ошибка: {error}")


def get_share_button(device: Device) -> UiObject:
    """Получение кнопки 'Поделится'"""
    logging.info("Поиск кнопки 'Поделится'")
    try:
        return device(
            resourceId=XmlIdEnum.MENU_SHARE,
            className=XmlClassEnum.BUTTON
        )
    except Exception as error:
        logging.error(f"Не удалось найти кнопку 'Поделится', ошибка: {error}")


def get_note_button(device: Device) -> UiObject:
    """Получение кнопки 'Копировать'"""
    logging.info("Поиск кнопки 'Копировать'")
    try:
        return device(
            text='Копировать',
            resourceId="android:id/text1",
            className="android.widget.TextView"
        )
    except Exception as error:
        logging.error(f"Не удалось найти кнопку 'Копировать', ошибка: {error}")


def get_edit_text(device: Device) -> str:
    return device(className="android.widget.EditText").long_click()


def get_url_from_app_url(device: Device) -> str:
    return device(className="android.widget.EditText").info['text']
