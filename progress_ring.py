import flet as ft
import time

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    pr1 = ft.ProgressRing(
        value=0,
        stroke_width=20,
        color=ft.colors.GREEN,
        bgcolor=ft.colors.GREEN_100,
        tooltip='Carregando',
    )

    pr2 = ft.ProgressRing(
        stroke_width=20,
    )

    page.add(pr1, pr2)

    for i in range(100):
        pr1.value += 0.01
        time.sleep(0.2)
        page.update()

if __name__ == '__main__':
    ft.app(target=main)
