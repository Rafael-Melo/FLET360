import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    rsl = ft.RangeSlider(
        start_value=40,
        end_value=80,
        active_color=ft.colors.AMBER,
        inactive_color=ft.colors.RED,
        overlay_color=ft.colors.TEAL,
        divisions=12,
        label='Slider {value}',
        min=20,
        max=150,
        round=2,
        on_change=lambda _: print(rsl.start_value, '->', rsl.end_value)
    )

    page.add(rsl)


if __name__ == '__main__':
    ft.app(target=main)