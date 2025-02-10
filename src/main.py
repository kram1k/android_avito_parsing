from uiautomator2 import connect, Direction
from core.utils import (
    write_xml,
    get_button_container,
    get_search_container,
    get_search_list_item,
    get_button_search,
    get_cords_swipe_down,
    get_toggle_date_button,
    get_accept_button
)
from core.constants import DELAY, AVITO, SEARCH_TEXT


def main():
    phone = connect()
    phone.implicitly_wait(DELAY)
    phone.app_start(AVITO, use_monkey=True)
    get_button_container(phone).click()
    get_search_container(phone).set_text(SEARCH_TEXT)
    get_search_list_item(phone).click()
    get_button_search(phone).click()
    get_cords_swipe_down(phone)
    get_toggle_date_button(phone).click()
    get_accept_button(phone).click()
    # write_xml(phone, "search_list_hierarchy.xml")
    # fx=h_1, fy=w_1, tx=h_2, ty=w_2,
    #     .child_by_text(txt="По дате", resourceId="com.avito.android:id/design_item_title", allow_scroll_search=True, className="android.widget.TextView")



if __name__ == "__main__":
    main()
