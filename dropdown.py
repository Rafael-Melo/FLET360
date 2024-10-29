import flet as ft

def main(page: ft.Page):
    dd = ft.Dropdown(
        label='Selecione uma opção',
        options=[
            ft.dropdown.Option(key=1, text='Opção 01'),
            ft.dropdown.Option(key=2, text='Opção 02'),
            ft.dropdown.Option(key=3, text='Opção 03'),
            ft.dropdown.Option(key=4, text='Opção 04', disabled=True),
            ft.dropdown.Option(key=5, text='Opção 05'),
        ],
        value=2,
        filled=True,
        bgcolor=ft.colors.RED,
        border=ft.InputBorder.OUTLINE,
        border_color=ft.colors.GREEN,
        border_width=5,
        border_radius=ft.border_radius.all(20),
        color=ft.colors.YELLOW,
        content_padding=50,
        alignment=ft.alignment.center,
        width=180,
    )

    page.add(dd, dd)


if __name__ == '__main__':
    ft.app(target=main)
