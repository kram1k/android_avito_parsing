import logging
import os

from uiautomator2 import connect
from dotenv import load_dotenv
from telebot import TeleBot

from core.actions.getters import (
    get_button_container,
    get_info_about_ad,
)
from core.actions.clicks import (
    click_search_list_item,
)
from core.actions.processes import (
    filter_setting,
    fill_empty_dict,
    parse_url,
    delay_and_update_screen,
    update_ad_dict
)
from core.validations import is_not_empty_ads, is_new_ad
from core.constants import StrEnum, FloatEnum
from core.log_config import configure_logging

logger = logging.getLogger(__name__)
configure_logging()

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = TeleBot(token=TELEGRAM_TOKEN)


def parsing_process(
    tg_user_id: int | str,
    phone_id: str = "",
    search_query: str = StrEnum.SEARCH_TEXT
):
    """Основная логика работы парсера"""
    configure_logging()
    phone = connect(phone_id)
    phone.implicitly_wait(FloatEnum.DELAY_WIDGET)
    phone.app_start(StrEnum.AVITO, use_monkey=True)
    get_button_container(phone).click()
    get_button_container(phone).set_text(search_query)
    click_search_list_item(phone)
    filter_setting(phone)

    advertisements: dict[str, list] = {
        "id": [],
        "t_pub": [],
    }
    while:
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
                bot.send_message(message, chat_id=int(tg_user_id))
                advertisements = update_ad_dict(
                    advertisements,
                    ad_id, t_pub)
