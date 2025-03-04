import logging
from time import sleep

from uiautomator2 import Device, Direction

from core.actions.swipes import cords_swipe_down

from core.actions.clicks import (
    click_button_filter,
    click_toggle_date_button,
    click_accept_button,
    long_click_to_edit_text,
    click_paste_url_in_input,
    click_select_all_url,
    click_delete_url_in_input,
    click_to_announcement,
    click_share_button,
    click_copy_button,
)
from core.actions.getters import (
    get_url_from_app_url,
    get_info_about_ad,
    UniqueId,
    TimePublish,
)


from core.constants import (
    IntEnum,
    StrEnum,
    FloatEnum
)


def filter_setting(device: Device):
    """Настройка фильтра поиска"""
    click_button_filter(device)
    cords_swipe_down(device)
    click_toggle_date_button(device)
    sleep(IntEnum.WAIT_END_OPERTION)
    click_accept_button(device)
    sleep(IntEnum.WAIT_END_OPERTION)


def parse_url(device: Device) -> str:
    """Работа приложения для извлечения ссылки"""
    click_to_announcement(device, 0)
    sleep(IntEnum.WAIT_END_OPERTION)
    click_share_button(device)
    click_copy_button(device)
    device.app_start(StrEnum.URL_APP, use_monkey=True)
    sleep(IntEnum.WAIT_APP_START)
    long_click_to_edit_text(device)
    click_paste_url_in_input(device)
    sleep(IntEnum.WAIT_END_OPERTION)
    link = get_url_from_app_url(device)
    sleep(IntEnum.WAIT_END_OPERTION)
    long_click_to_edit_text(device)
    click_select_all_url(device)
    sleep(IntEnum.WAIT_END_OPERTION)
    click_delete_url_in_input(device)
    device.app_start(StrEnum.AVITO, use_monkey=True)
    sleep(2)
    device.press(StrEnum.BACK)
    return link


def fill_empty_dict(device: Device, ad: dict[str, list]):
    """Заполнение списка новыми обявлениями"""
    logging.info(fill_empty_dict.__doc__)
    try:
        for i in range(2):
            click_to_announcement(device, i)
            obj = get_info_about_ad(device)
            ad["id"].append(obj[0])
            ad["t_pub"].append(obj[1])
        return ad
    except Exception as error:
        logging.error(f"Не удалось заполнить список, ошибка {error}")


def delay_and_update_screen(device: Device):
    """Ожидание и обновления экрана"""
    logging.info(delay_and_update_screen.__doc__)
    sleep(FloatEnum.DELAY_SCREEN)
    device().swipe(Direction.DOWN)
    sleep(IntEnum.WAIT_END_OPERTION)
    click_to_announcement(device, 0)
    sleep(IntEnum.WAIT_END_OPERTION)


def update_ad_dict(
    ad: dict[str, list],
    ad_id: int | UniqueId,
    t_pub: str | TimePublish,
) -> dict[str, list]:
    ad["id"][-1] = ad["id"][0]
    ad["t_pub"][-1] = ad["t_pub"][0]
    ad["id"][0] = ad_id
    ad["t_pub"][0] = t_pub
    return ad
