from typing import Any

import flet as ft

from ui.constants import TextEnum

main_text = ft.Text(
    TextEnum.MAIN_TEXT, size=55,
    weight=ft.FontWeight.W_900,
)
text_search_query = ft.Text(
    TextEnum.TEXT_SEARCH_QUERY,
    size=30,
    weight=ft.FontWeight.BOLD,
)
text_chat_id = ft.Text(
    TextEnum.TEXT_CHAT_ID,
    size=30,
    weight=ft.FontWeight.BOLD
)
text_phone_id = ft.Text(
    TextEnum.TEXT_PHONE_ID,
    size=30,
    weight=ft.FontWeight.BOLD
)