from time import sleep
from pprint import pprint
from typing import Any

from uiautomator2 import connect

from core.actions.clicks import click_to_announcement
from core.actions.getters import get_info_about_ad, UniqueId, TimePublish, Views

phone = connect()
advertisements: dict[str, list[Any]] = {
    "id": [],
    "time_publish": [],
    "views": []
}

new_targets = 0
while new_targets < 1:
    for index in range(2):
        click_to_announcement(phone, index)
        obj = get_info_about_ad(phone)
        advertisements["id"].append(obj[0])
        advertisements["time_publish"].append(obj[1])
        advertisements["time_publish"].append(obj[2])
    break
print(advertisements)
