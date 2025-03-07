import flet as ft

from dev import CounterApp


def main(page: ft.Page):
    app = CounterApp(page)


if __name__ == "__main__":
    ft.app(target=main)
