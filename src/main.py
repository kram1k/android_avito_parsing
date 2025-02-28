import logging
from time import sleep

from uiautomator2 import connect

from core.getters import (
    # write_xml,
    get_url_from_app_url,
    get_button_container,
)
from core.swipes import cords_swipe_down
from core.clicks import (
    click_search_list_item,
    click_button_filter,
    click_toggle_date_button,
    click_accept_button,
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
