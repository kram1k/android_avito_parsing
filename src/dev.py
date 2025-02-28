from time import sleep

from uiautomator2 import connect

from core.activities import (
    long_click_to_edit_text,
    # write_xml,
    paste_url_in_input,
    get_url_from_app_url,
    select_all_url,
    delete_url_in_input
)
from core.utils import append_link_to_file

phone = connect()
long_click_to_edit_text(phone)
paste_url_in_input(phone)
append_link_to_file(link=get_url_from_app_url(phone))
long_click_to_edit_text(phone)
select_all_url(phone)
delete_url_in_input(phone)
