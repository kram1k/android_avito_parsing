import logging
from time import sleep

from uiautomator2 import Device, UiObject, Direction

from .constants import StrEnum, IntEnum

logger_2 = logging.getLogger(__name__)
logger_2.setLevel(logging.INFO)
handler2 = logging.FileHandler(f"{__name__}.log", mode='w')
formatter2 = logging.Formatter(
    "%(name)s %(asctime)s %(levelname)s %(message)s"
)
handler2.setFormatter(formatter2)
logger_2.addHandler(handler2)


def write_xml(device: Device, file: str) -> None:
    """Запись элементов экрана в формате xml в файл"""

    logging.info("Запись файла")
    try:
        with open(file, "w", encoding=StrEnum.UTF) as f:
            f.write(device.dump_hierarchy())
            f.close
    except Exception as error:
        logging.error(
            f"Не удалось записать dump в файл {file}, ошибка {error}"
        )


def get_button_container(device: Device) -> UiObject:
    """Получение кнопки input для поиска"""

    logging.info("Поиск кнопки поиска")
    try:
        return device(
            text=StrEnum.RU_SEARCH_TEXT,
            resourceId="",
            className=StrEnum.CLASS_EDIT_TEXT
        )
    except Exception as error:
        logging.error(f"Не удалось найти поле, ошибка {error}")


def get_search_list_item(device: Device) -> UiObject:
    """Получение элемента из поисковой выдачи"""

    logging.info("Поиск элемента в поисковой выдачи")
    try:
        return device(
            text=StrEnum.SEARCH_TEXT,
            resourceId=StrEnum.ID_SUGGEST_TITLE,
            className=StrEnum.CLASS_TEXT_VIEW
        )
    except Exception as error:
        logging.error(f"Не удалось найти элемент, ошибка {error}")


def get_button_filter(device: Device) -> UiObject:
    """Получение кнопки для настройки фильтрации"""

    logging.info("Поиск кнопки фильтра")
    try:
        return device(
            text=StrEnum.FILTER_BUTTON,
            className=StrEnum.CLASS_TEXT_VIEW,
            resourceId=StrEnum.ID_FILTERS_TEXT
        )
    except Exception as error:
        logging.error(f"Не удалось найти кнопку, ошибка {error}")


def get_cords_swipe_down(device: Device) -> None:
    """Прокрутка экрана до нужного компонента"""
    logging.info("Начало оперции прокрутки...")
    for _ in range(IntEnum.COUNT_SCROLLS):
        device(
            resourceId=StrEnum.ID_CONTENT,
            className=StrEnum.CLASS_FRAME_LAYOUT) \
            .swipe(direction=Direction.UP, steps=IntEnum.TIME_TO_SCROLL)
    logging.info("Ожидание ее окончания")
    sleep(IntEnum.WAIT_SCROLL_DONE)


def get_toggle_date_button(device: Device) -> UiObject:
    """Измение сортировки на режим 'По дате'"""
    logging.info(f"Поиск кнопки для фильтрации: {StrEnum.TO_DATE}")
    try:
        return device(
            resourceId=StrEnum.ID_FILTERS_SCREEN_ROOT,
            className=StrEnum.CLASS_FRAME_LAYOUT) \
            .child_by_text(
                txt=StrEnum.TO_DATE,
                resourceId=StrEnum.ID_DESIGN_ITEM_TITLE,
                allow_scroll_search=True,
                className=StrEnum.CLASS_TEXT_VIEW
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
                resourceId=StrEnum.ID_TEXT_VIEW,
                className=StrEnum.CLASS_TEXT_VIEW
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
            resourceId=StrEnum.ID_RECYCLER_VIEW_ID,
            className=StrEnum.CLASS_RECYCLER_VIEW_CLASS).child_by_text(
                txt=text
            )
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
