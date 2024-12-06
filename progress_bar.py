import flet as ft
import time

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    pb1 = ft.ProgressBar(
        value=0,
        bar_height=10,
        color=ft.colors.RED,
        bgcolor=ft.colors.RED_100,
        tooltip='Barra de Progresso',
    )

    pb2 = ft.ProgressBar(
        bar_height=10
    )

    for i in range(10):
        pb1.value += 0.1
        time.sleep(1)
        page.update()

    page.add(pb1, pb2)

if __name__ == '__main__':
    ft.app(target=main)
