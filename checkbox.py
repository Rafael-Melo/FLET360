import flet as ft

def main(page: ft.Page):
    cb = ft.Checkbox(
        label='Selecione aqui',
        label_position=ft.LabelPosition.LEFT,
        check_color=ft.colors.AMBER,
        fill_color={
            ft.MaterialState.HOVERED: ft.colors.GREEN,
            ft.MaterialState.FOCUSED: ft.colors.RED,
            ft.MaterialState.DEFAULT: ft.colors.BLACK,
        },
        tristate=True,
        value=True,
        on_change=lambda _: print('O valor agora é', cb.value)
    )

    page.add(cb)


if __name__ == '__main__':
    ft.app(target=main)
