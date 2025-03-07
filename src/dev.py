import flet as ft

from ui.constants import TextEnum
from ui.text import main_text
from ui.rows import (
    row_chat_id,
    row_phone_id,
    row_search_query,
    row_buttons
)

button = ft.Button()


def main(page: ft.Page):
    page.title = TextEnum.MAIN_TEXT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    column = ft.Column([
        main_text,
        row_chat_id,
        row_phone_id,
        row_search_query,
        row_buttons

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
