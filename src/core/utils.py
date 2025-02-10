from time import sleep

from uiautomator2 import Device, UiObject, Direction
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
    FILTERS_TEXT,
    CONTENT,
    FRAME_LAYOUT,
    TIME_TO_SCROLL,
    FILTERS_SCREEN_ROOT,
    TO_DATE,
    DESIGN_ITEM_TITLE,
    WAIT_SCROLL_DONE,
    ID_TEXT_VIEW,
    ACCEPT_BUTTON
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


def get_cords_swipe_down(device: Device) -> None:
    device(resourceId=CONTENT, className=FRAME_LAYOUT) \
        .swipe(direction=Direction.UP, steps=TIME_TO_SCROLL)
    device(resourceId=CONTENT, className=FRAME_LAYOUT) \
        .swipe(direction=Direction.UP, steps=TIME_TO_SCROLL)
    device(resourceId=CONTENT, className=FRAME_LAYOUT) \
        .swipe(direction=Direction.UP, steps=TIME_TO_SCROLL)
    sleep(WAIT_SCROLL_DONE)


def get_toggle_date_button(device: Device) -> UiObject:
    return device(resourceId=FILTERS_SCREEN_ROOT, className=FRAME_LAYOUT) \
        .child_by_text(
            txt=TO_DATE,
            resourceId=DESIGN_ITEM_TITLE,
            allow_scroll_search=True,
            className=TEXT_VIEW
        )


def get_accept_button(device: Device) -> UiObject:
    return device(resourceId=FILTERS_SCREEN_ROOT, className=FRAME_LAYOUT) \
        .child_by_text(
            txt=ACCEPT_BUTTON,
            resourceId=ID_TEXT_VIEW,
            allow_scroll_search=True,
            className=TEXT_VIEW
        )
