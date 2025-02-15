import logging
from time import sleep

from uiautomator2 import Device, UiObject, Direction
from core.constants import (
    SEARCH_VIEW_CONTAINER,
    TOOLBAR_CONTAINER,
    CONTAINER,
    INPUT_VIEW,
    RU_SEARCH_TEXT,
    UTF,
    SUGGESTS_RECYCLER_VIEW,
    SEARCH_VIEW_ITEM,
    ICON_CONTAINER,
    LINEAR_LAYOUT,
    TEXT_VIEW,
    FILTER_BUTTON,
    FILTERS_TEXT,
    CONTENT,
    FRAME_LAYOUT,
    TIME_TO_SCROLL,
    FILTERS_SCREEN_ROOT,
    TO_DATE,
    DESIGN_ITEM_TITLE,
    WAIT_SCROLL_DONE,
    ID_TEXT_VIEW,
    ACCEPT_BUTTON,
    RECYCLER_VIEW_ID,
    RECYCLER_VIEW_CLASS
)

logger_2 = logging.getLogger(__name__)
logger_2.setLevel(logging.INFO)
handler2 = logging.FileHandler(f"{__name__}.log", mode='w')
formatter2 = logging.Formatter(
    "%(name)s %(asctime)s %(levelname)s %(message)s"
)
handler2.setFormatter(formatter2)
logger_2.addHandler(handler2)


def write_xml(device: Device, xml: str) -> None:
    """Запись элементов экрана в формате xml в файл"""

    logging.info("Запись файла")
    try:
        with open(xml, "w", encoding=UTF) as f:
            f.write(device.dump_hierarchy())
            f.close
    except Exception as error:
        logging.error(
            f"Не удалось записать dump в файл {xml}, ошибка {error}"
        )


def get_search_container(device: Device) -> UiObject:
    """Получение формы для ввода запроса для поиска"""

    logging.info("Поиск формы поиска")
    try:
        return device(resourceId=SEARCH_VIEW_CONTAINER) \
            .child(resourceId=TOOLBAR_CONTAINER) \
            .child(resourceId=CONTAINER) \
            .child(resourceId=INPUT_VIEW) \
            .child(text=RU_SEARCH_TEXT)
    except Exception as error:
        logging.error(f"Не удалось найти контейнер, ошибка {error}")


def get_button_container(device: Device) -> UiObject:
    """Получение кнопки input для поиска"""

    logging.info("Поиск кнопки поиска")
    try:
        return device(resourceId=SEARCH_VIEW_CONTAINER) \
            .child(resourceId=TOOLBAR_CONTAINER) \
            .child(resourceId=CONTAINER) \
            .child(resourceId=INPUT_VIEW)
    except Exception as error:
        logging.error(f"Не удалось найти поле, ошибка {error}")


def get_search_list_item(device: Device) -> UiObject:
    """Получение элемента из поисковой выдачи"""

    logging.info("Поиск элемента в поисковой выдачи")
    try:
        return device(resourceId=SUGGESTS_RECYCLER_VIEW) \
            .child(resourceId=SEARCH_VIEW_ITEM) \
            .child(resourceId=ICON_CONTAINER, className=LINEAR_LAYOUT)
    except Exception as error:
        logging.error(f"Не удалось найти элемент, ошибка {error}")


def get_button_filter(device: Device) -> UiObject:
    """Получение кнопки для настройки фильтрации"""

    logging.info("Поиск кнопки фильтра")
    try:
        return device(
            text=FILTER_BUTTON,
            className=TEXT_VIEW,
            resourceId=FILTERS_TEXT
        )
    except Exception as error:
        logging.error(f"Не удалось найти кнопку, ошибка {error}")


def get_cords_swipe_down(device: Device) -> None:
    """Прокрутка экрана до нужного компонента"""
    logging.info("Начало оперции прокрутки...")
    device(resourceId=CONTENT, className=FRAME_LAYOUT) \
        .swipe(direction=Direction.UP, steps=TIME_TO_SCROLL)
    device(resourceId=CONTENT, className=FRAME_LAYOUT) \
        .swipe(direction=Direction.UP, steps=TIME_TO_SCROLL)
    device(resourceId=CONTENT, className=FRAME_LAYOUT) \
        .swipe(direction=Direction.UP, steps=TIME_TO_SCROLL)
    logging.info("Ожидание ее окончания")
    sleep(WAIT_SCROLL_DONE)


def get_toggle_date_button(device: Device) -> UiObject:
    """Измение сортировки на режим 'По дате'"""
    logging.info(f"Поиск кнопки для фильтрации: {TO_DATE}")
    try:
        return device(resourceId=FILTERS_SCREEN_ROOT, className=FRAME_LAYOUT) \
            .child_by_text(
                txt=TO_DATE,
                resourceId=DESIGN_ITEM_TITLE,
                allow_scroll_search=True,
                className=TEXT_VIEW
            )
    except Exception as error:
        logging.error(
            f"Не удалось найти кнопку-переключатель {TO_DATE}, ошибка {error}"
        )


def get_accept_button(device: Device) -> UiObject:
    """Подтверждение изменений в филтре поиска"""
    logging.info("Поиск кнопки подтверждения изменений")
    try:
        return device(resourceId=FILTERS_SCREEN_ROOT, className=FRAME_LAYOUT) \
            .child_by_text(
                txt=ACCEPT_BUTTON,
                resourceId=ID_TEXT_VIEW,
                allow_scroll_search=True,
                className=TEXT_VIEW
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
            resourceId=RECYCLER_VIEW_ID,
            className=RECYCLER_VIEW_CLASS).child_by_text(txt=text)
    except Exception as error:
        logging.error(f"Не удалось найти новый объект, ошибка: {error}")


def get_share_button(device: Device) -> UiObject:
    """Получение кнопки 'Поделится'"""
    logging.info("Поиск кнопки 'Поделится'")
    try:
        return device(
            resourceId="com.avito.android:id/menu_share",
            className="android.widget.Button"
        )
    except Exception as error:
        logging.error(f"Не удалось найти кнопку 'Поделится', ошибка: {error}")


def get_note_button(device: Device) -> UiObject:
    """Получение кнопки 'Заметки'"""
    logging.info("Поиск кнопки 'Заметки'")
    try:
        return device(
            text='Заметки',
            resourceId="android:id/text1",
            className="android.widget.TextView"
        )
    except Exception as error:
        logging.error(f"Не удалось найти кнопку 'Заметки', ошибка: {error}")


def get_url_from_note(device: Device) -> str:
    return device(resourceId="com.miui.notes:id/rich_editor", className="android.widget.EditText").info['text']
