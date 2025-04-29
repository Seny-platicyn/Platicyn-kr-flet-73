import flet as ft
from datetime import datetime
import os


def main(page: ft.Page):
    page.title = "Счётчик кликов"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    counter = ft.Ref[int]()
    counter.current = 0

    txt_count = ft.Ref[ft.Text]()
    btn_save = ft.Ref[ft.ElevatedButton]()

    def update_display():
        txt_count.current.value = f"Кликов: {counter.current}"
        page.update()

    def increment(e):
        counter.current += 1
        update_display()

    def reset(e):
        counter.current = 0
        update_display()

    def save(e):
        try:

            file_path = os.path.join(os.getcwd(), "click_history.txt")

            with open(file_path, "a", encoding="utf-8") as f:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"{timestamp}: {counter.current} кликов\n")

            btn_save.current.text = "Сохранено!"
            print(f"Файл сохранён: {file_path}")
        except Exception as ex:
            btn_save.current.text = f"Ошибка: {str(ex)}"
            print(f"Ошибка сохранения: {ex}")

        page.update()

    page.add(
        ft.Column(
            [
                ft.Text(ref=txt_count, size=40, weight="bold"),
                ft.Row(
                    [
                        ft.ElevatedButton("+1 Клик", on_click=increment),
                        ft.ElevatedButton("Сброс", on_click=reset, color="red"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.ElevatedButton(
                    ref=btn_save,
                    text="Сохранить в TXT",
                    on_click=save,
                    icon=ft.icons.SAVE,
                ),
            ],
            spacing=20,
        )
    )
    update_display()


ft.app(target=main)