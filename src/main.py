from uiautomator2 import connect


from core.utils import get_button_container, \
    get_search_container, \
    get_search_list_item, \
    get_button_search \
    # write_xml, \
    
from core.constants import DELAY, AVITO, SEARCH_TEXT


def main():
    device = connect()
    device.implicitly_wait(DELAY)
    device.app_start(AVITO, use_monkey=True)
    get_button_container(device).click()
    get_search_container(device).set_text(SEARCH_TEXT)
    get_search_list_item(device).click()
    get_button_search(device).click()
    
    # write_xml(device, "list_hierarchy.xml")


if __name__ == "__main__":
    main()
