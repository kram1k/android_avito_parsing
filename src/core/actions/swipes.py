import logging
from time import sleep

from uiautomator2 import Device, Direction

from ..constants import (
    IntEnum, XmlIdEnum,
    XmlClassEnum
)


def cords_swipe_down(device: Device) -> None:
    """Прокрутка экрана до нужного компонента"""
    logging.info(cords_swipe_down.__doc__)
    for _ in range(IntEnum.COUNT_SCROLLS):
        device(
            resourceId=XmlIdEnum.CONTENT,
            className=XmlClassEnum.FRAME_LAYOUT) \
            .swipe(direction=Direction.UP, steps=IntEnum.TIME_TO_SCROLL)
    logging.info("Ожидание ее окончания")
    sleep(IntEnum.WAIT_SCROLL_DONE)
