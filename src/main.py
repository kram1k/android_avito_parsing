import logging
import sys

from uiautomator2 import connect
from core.utils import (
    write_xml,
    get_button_container,
    get_search_container,
    get_search_list_item,
    get_button_filter,
    get_cords_swipe_down,
    get_toggle_date_button,
    get_accept_button
)
from core.constants import DELAY, AVITO, SEARCH_TEXT


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
    phone.implicitly_wait(DELAY)
    phone.app_start(AVITO, use_monkey=True)
    get_button_container(phone).click()
    get_search_container(phone).set_text(SEARCH_TEXT)
    get_search_list_item(phone).click()
    get_button_filter(phone).click()
    get_cords_swipe_down(phone)
    get_toggle_date_button(phone).click()
    get_accept_button(phone).click()
    
    # new_elements = 0
    # first_screen: list[str] = []
    # second_screen: list[str] = []
    # while new_elements <= 5:
    #     if first_screen and second_screen:
    #         ...
    #     else:
    #         ...
    # write_xml(phone, "new_list_hierarchy.xml")
    # fx=h_1, fy=w_1, tx=h_2, ty=w_2,
    #     .child_by_text(txt="По дате", resourceId="com.avito.android:id/design_item_title", allow_scroll_search=True, className="android.widget.TextView")



if __name__ == "__main__":
    main()
