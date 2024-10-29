import flet as ft

def main(page: ft.Page):
    sl = ft.Slider(

    )

    page.add(sl)


if __name__ == '__main__':
    ft.app(target=main)