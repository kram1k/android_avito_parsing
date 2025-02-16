import logging
from time import sleep

from uiautomator2 import connect
from core.activities import (
    write_xml,
    # get_note_button,
    # get_url_from_note,
    get_button_container,
    get_search_list_item,
    get_button_filter,
    get_cords_swipe_down,
    get_toggle_date_button,
    get_accept_button,
    # swipe_screen,
    # get_new_item,
    # get_share_button
)
from core.constants import (
    IntEnum,
    StrEnum,
    FloatEnum
)
# from core.xmlparse import create_list


def main():
    """Основная логика работы парсера"""
    logger_1 = logging.getLogger(__name__)
    logger_1.setLevel(logging.INFO)
    handler2 = logging.FileHandler(f"{__name__}.log", mode='w')
    formatter2 = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
    handler2.setFormatter(formatter2)
    logger_1.addHandler(handler2)
    logger_1.info(f"Testing the custom logger for module {__name__}...")

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

    # new_elements = 0
    # first_screen: list[str] = []
    # second_screen: list[str] = []
    # while new_elements <= 1:
    #     if first_screen == [] and second_screen == []:
    #         write_xml(phone, FIRST_SCREEN)
    #         first_screen = create_list(FIRST_SCREEN)
    #         sleep(DELAY_SCREEN)
    #         swipe_screen(phone)
    #         write_xml(phone, SECOND_SCREEN)
    #         second_screen = create_list(SECOND_SCREEN)
    #     else:
    #         if second_screen == first_screen:
    #             second_screen = first_screen
    #             first_screen.clear()
    #         else:
    #             get_new_item(phone, second_screen[0]).click()
    #             get_share_button(phone).click()
    #             get_note_button(phone).click()
    #             print(get_url_from_note(phone))
    #             new_elements += 1
    #             phone.press.back()
    #             phone.press.back()
    # write_xml(phone, "hierarchy.xml")




if __name__ == "__main__":
    main()
