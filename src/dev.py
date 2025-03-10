import flet as ft

from ui.constants import TextEnum
from ui.text import main_text
from ui.rows import (
    row_chat_id,
    row_phone_id,
    row_search_query,
)
from ui.buttons import btn_submit
from ui.text_fields import (
    field_search_query,
    field_chat_id,
    field_phone_id
)

  
def main(page: ft.Page):

    page.title = TextEnum.MAIN_TEXT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    chat_id = ft.Text()
    phone_id = ft.Text()
    search_query = ft.Text()

    def click_btn_submit(e):
        chat_id.value = field_chat_id.value
        phone_id.value = field_phone_id.value
        search_query.value = field_search_query.value
        field_search_query.value, field_phone_id.value, field_chat_id.value = (
            "", "", ""
        )
        page.update()

    btn_submit.on_click = click_btn_submit

    column = ft.Column([
        main_text,
        row_chat_id,
        row_phone_id,
        row_search_query,
        btn_submit
    ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [column]
                ),
                width=900,
                padding=30,
                alignment=ft.alignment.center,
            ),
        )
    main_column = ft.Column([
        card,
    ])
    page.add(main_column)


if __name__ == "__main__":
    ft.app(main)
