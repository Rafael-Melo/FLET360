import flet as ft

def main(page: ft.Page):
    sa = ft.SafeArea(
        content=ft.Container(gbcolor=ft.Colors.AMBER),
        expand=True,
        bottom=True,
        left=True,
        right=True,
        top=True,
        minimum=50,
    )

    page.add(sa)
    # Para identificar áreas não utlilizáveis nos smatphones


if __name__ == '__main__':
    ft.app(target=main)