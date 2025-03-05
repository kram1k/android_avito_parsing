import flet as ft
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def main(page: ft.Page):
    # Текстовые поля
    chat_id = ft.TextField(label="Идентификатор чата в Telegram")
    serial_number = ft.TextField(
        label="Серийный номер телефона",
        can_reveal_password=True,
        password=True
    )
    search_query = ft.TextField(label="Поисковый запрос")

    # Кнопка отправки
    button_submit = ft.OutlinedButton("Отправить")

    # Столбец для основных элементов
    column = ft.Column(
        controls=[
            chat_id,
            serial_number,
            search_query,
            button_submit
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        width=500,
        height=700,
    )

    container = ft.Container(
        content=column,
        alignment=ft.alignment.center,
        expand=True
    )

    page.add(container)


ft.app(target=main)
