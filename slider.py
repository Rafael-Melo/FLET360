import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    sl = ft.Slider(
        active_color=ft.colors.AMBER,
        inactive_color=ft.colors.RED,
        thumb_color=ft.colors.GREEN,
        divisions=10,
        label= 'Slider {value}',
        min=0,
        max=100,
        round=2, # Casas decimais
        value=10,
        on_change=lambda _: print('Selecionado', sl.value)
    )

    page.add(sl)


if __name__ == '__main__':
    ft.app(target=main)