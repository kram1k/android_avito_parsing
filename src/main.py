import logging
import os
import threading

import flet as ft
from dotenv import load_dotenv
from telebot import TeleBot
from uiautomator2 import connect

from core.actions.clicks import click_search_list_item
from core.actions.getters import get_button_container, get_info_about_ad
from core.actions.processes import (delay_and_update_screen, fill_empty_dict,
                                    filter_setting, parse_url, update_ad_dict)
from core.constants import FloatEnum, StrEnum
from core.log_config import configure_logging
from core.validations import is_new_ad, is_not_empty_ads
from ui.buttons import btn_start_stop
from ui.constants import TextEnum
from ui.rows import row_chat_id, row_phone_id, row_search_query, row_btn
from ui.text import main_text
from ui.text_fields import field_chat_id, field_phone_id, field_search_query

logger = logging.getLogger(__name__)
configure_logging()

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = TeleBot(token=TELEGRAM_TOKEN)


def main(page: ft.Page):
    is_running = False
    phone_connected = False
    # Parsing

    def parsing():
        nonlocal phone_connected
        advertisements = {
            "id": [],
            "t_pub": [],
            }
        while is_running:
            if phone_connected is False:
                phone = connect(phone_id.value)
                phone.implicitly_wait(FloatEnum.DELAY_WIDGET)
                phone.app_start(StrEnum.AVITO, use_monkey=True)
                get_button_container(phone).click()
                get_button_container(phone).set_text(search_query.value)
                click_search_list_item(phone, search_query.value)
                filter_setting(phone)
                phone_connected = True
            if is_not_empty_ads(advertisements):
                logging.info("Список обьявлнений пуст")
                advertisements = fill_empty_dict(phone, advertisements)
            else:
                logging.info("Список обьявлнений не пуст")
                delay_and_update_screen(phone)
                ad_id, t_pub = get_info_about_ad(phone)
                if is_new_ad(advertisements, ad_id):
                    logging.info("Нет нового обьявления")
                    continue
                else:
                    logging.info("Новое обьявление найдено")
                    link = parse_url(phone)
                    message = f"Ссылка: {link}\nВремя публикации: {t_pub}"
                    bot.send_message(message, chat_id=int(chat_id.value))
                    advertisements = update_ad_dict(
                        advertisements,
                        ad_id, t_pub)
    # UI
    page.title = TextEnum.MAIN_TEXT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    state_parsing = ft.Text(value="No activite", size=15)
    chat_id = ft.Text()
    phone_id = ft.Text()
    search_query = ft.Text()
    stop_event = threading.Event()

    def click_btn_start_stop(e):
        nonlocal is_running
        chat_id.value = field_chat_id.value
        phone_id.value = field_phone_id.value
        search_query.value = field_search_query.value
        field_search_query.value, field_phone_id.value, field_chat_id.value = (
            "", "", ""
        )
        page.update()
        if not is_running:
            is_running = True
            stop_event.clear()
            threading.Thread(target=parsing, daemon=True).start()
            btn_start_stop.text = "Stop"
            page.update()
        else:
            is_running = False
            stop_event.set()
            btn_start_stop.text = "Start"
            page.update()

    btn_start_stop.on_click = click_btn_start_stop

    column = ft.Column([
        main_text,
        row_chat_id,
        row_phone_id,
        row_search_query,
        row_btn,
        state_parsing,
        btn_start_stop
    ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    card_form = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [column]
                ),
                width=900,
                padding=30,
                alignment=ft.alignment.center,
            ),
        )
    page.add(card_form)


if __name__ == "__main__":
    ft.app(main)
