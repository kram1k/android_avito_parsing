import flet as ft

from ui.text import text_chat_id, text_phone_id, text_search_query
from ui.text_fields import field_chat_id, field_phone_id, field_search_query

row_chat_id = ft.Row([text_chat_id, field_chat_id])
row_phone_id = ft.Row([text_phone_id, field_phone_id])
row_search_query = ft.Row([text_search_query, field_search_query])
row_btn = ft.Row([], alignment=ft.MainAxisAlignment.CENTER)
