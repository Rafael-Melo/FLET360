import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    bg1 = ft.Badge(
        bgcolor=ft.colors.RED,
        content=ft.Icon(name = ft.icons.NOTIFICATIONS, size=300),
        label_visible=True,
        alignment=ft.alignment.top_right,
        small_size=30, # Só funciona quando não tem texto na label
        text='10',
        text_color=ft.colors.WHITE,
        text_style=ft.TextStyle(size=80, weight=ft.FontWeight.BOLD),
        large_size=100, # Altura
        padding=ft.padding.all(10),
    )

    page.add(bg1)


if __name__ == '__main__':
    ft.app(target=main)