import logging
from time import sleep
from typing import Any

from uiautomator2 import connect

from core.actions.getters import (
    get_info_about_ad,
    get_url_from_app_url,
    get_button_container,
)
from core.actions.swipes import cords_swipe_down
from core.actions.clicks import (
    click_search_list_item,
    click_button_filter,
    click_toggle_date_button,
    click_accept_button,
    click_to_announcement,
    long_click_to_edit_text,
    click_paste_url_in_input,
    click_select_all_url,
    click_delete_url_in_input,
)
from core.constants import (
    StrEnum,
    FloatEnum,
    IntEnum
)
from core.log_config import configure_logging
# from core.utils import append_link_to_file
logger = logging.getLogger(__name__)


def main():
    """Основная логика работы парсера"""
    configure_logging()
    phone = connect()
    phone.implicitly_wait(FloatEnum.DELAY_WIDGET)
    phone.app_start(StrEnum.AVITO, use_monkey=True)

    get_button_container(phone).click()
    get_button_container(phone).set_text(StrEnum.SEARCH_TEXT)
    click_search_list_item(phone)
    click_button_filter(phone)
    cords_swipe_down(phone)
    click_toggle_date_button(phone)
    sleep(IntEnum.WAIT_END_OPERTION)
    click_accept_button(phone)
    sleep(IntEnum.WAIT_END_OPERTION)
    advertisements = {
        "id": [],
        "time_publish": [],
        "views": []
    }

    new_targets = 0
    while new_targets < 1:
        if len(advertisements) != 0:
            for i in range(2):
                click_to_announcement(phone, i)
                obj = get_info_about_ad(phone)
                advertisements["id"].append(obj[0])
                advertisements["time_publish"].append(obj[1])
                advertisements["time_publish"].append(obj[2])
        else:
            ...
    # URL App work
    # sleep(IntEnum.WAIT_APP_START)
    # long_click_to_edit_text(phone)
    # paste_url_in_input(phone)
    # append_link_to_file(link=get_url_from_app_url(phone))
    # long_click_to_edit_text(phone)
    # select_all_url(phone)
    # delete_url_in_input(phone)
    # phone.app_start(StrEnum.AVITO, use_monkey=True)
    # phone.press("back")


if __name__ == "__main__":
    main()
