from uiautomator2 import Device, UiObject
from core.constants import (
    SEARCH_VIEW_CONTAINER,
    TOOLBAR_CONTAINER,
    CONTAINER,
    INPUT_VIEW,
    RU_SEARCH_TEXT,
    UTF,
    SUGGESTS_RECYCLER_VIEW,
    SEARCH_VIEW_ITEM,
    ICON_CONTAINER,
    LINEAR_LAYOUT, 
    TEXT_VIEW,
    FILTER_BUTTON,
    FILTERS_TEXT
)


def write_xml(device: Device, xml: str) -> None:
    with open(xml, 'w', encoding=UTF) as f:
        f.write(device.dump_hierarchy())
        f.close


def get_search_container(device: Device) -> UiObject:
    return device(resourceId=SEARCH_VIEW_CONTAINER) \
        .child(resourceId=TOOLBAR_CONTAINER) \
        .child(resourceId=CONTAINER) \
        .child(resourceId=INPUT_VIEW) \
        .child(text=RU_SEARCH_TEXT)


def get_button_container(device: Device) -> UiObject:
    return device(resourceId=SEARCH_VIEW_CONTAINER) \
        .child(resourceId=TOOLBAR_CONTAINER) \
        .child(resourceId=CONTAINER) \
        .child(resourceId=INPUT_VIEW)


def get_search_list_item(device: Device) -> UiObject:
    return device(resourceId=SUGGESTS_RECYCLER_VIEW) \
        .child(resourceId=SEARCH_VIEW_ITEM) \
        .child(resourceId=ICON_CONTAINER, className=LINEAR_LAYOUT)


def get_button_search(device: Device) -> UiObject:
    return device(
        text=FILTER_BUTTON,
        className=TEXT_VIEW,
        resourceId=FILTERS_TEXT
    )
