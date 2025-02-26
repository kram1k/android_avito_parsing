import logging
from time import sleep

from uiautomator2 import connect
from core.activities import (
    # write_xml,
    get_note_button,
    get_url_from_app_url,
    get_button_container,
    get_search_list_item,
    get_button_filter,
    get_cords_swipe_down,
    get_toggle_date_button,
    get_accept_button,
    swipe_screen,
    get_new_item,
    get_share_button
)
from core.constants import (
    StrEnum,
    FloatEnum,
    IntEnum
)
from core.log_config import configure_logging
from core.utils import fill_lists, append_link_to_file
logger = logging.getLogger(__name__)


def main():
    """Основная логика работы парсера"""
    configure_logging()
    phone = connect()
    phone.implicitly_wait(FloatEnum.DELAY_WIDGET)
    phone.app_start(StrEnum.AVITO, use_monkey=True)

    get_button_container(phone).click()
    get_button_container(phone).set_text(StrEnum.SEARCH_TEXT)
    get_search_list_item(phone).click()
    get_button_filter(phone).click()
    get_cords_swipe_down(phone)
    get_toggle_date_button(phone).click()
    sleep(2)
    get_accept_button(phone).click()
    sleep(2)

    new_elements = 0
    first_screen: list[str] = []
    second_screen: list[str] = []
    while new_elements <= 2:
        if first_screen == [] and second_screen == []:
            first_screen, second_screen = fill_lists(phone)
            first_screen = first_screen
            second_screen = second_screen
        else:
            if second_screen == first_screen:
                # logging.info("Новое обьвление не найденно!")
                # second_screen.clear()
                # first_screen.clear()
            # else:
                logging.info("Новое обьвление найденно!")
                get_new_item(phone, second_screen[0]).click()
                get_share_button(phone).click()
                get_note_button(phone).click()
                phone.app_start(StrEnum.URL_APP, use_monkey=True)
                
                sleep(IntEnum.WAIT_APP_START)
                append_link_to_file(get_url_from_app_url(phone))
                new_elements += 1
                phone.app_start(StrEnum.AVITO, use_monkey=True)
                phone.press.back()
                second_screen.clear()
                first_screen.clear()
    # write_xml(phone, "hierarchy.xml")


if __name__ == "__main__":
    main()
