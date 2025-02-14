import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER,
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER,

    def change_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        
        page.update()


    st = ft.Switch(
        active_color=ft.colors.GREEN,
        active_track_color=ft.colors.AMBER,
        inactive_thumb_color=ft.colors.BLACK,
        inactive_track_color=ft.colors.WHITE,
        label='Deseja ativar?',
        label_position=ft.LabelPosition.LEFT,

        thumb_color={
            ft.MaterialState.HOVERED: ft.colors.GREEN,
            ft.MaterialState.FOCUSED: ft.colors.RED,
            ft.MaterialState.DEFAULT: ft.colors.BLUE,
        },

        thumb_icon={
            ft.MaterialState.SELECTED: ft.icons.CHECK,
            ft.MaterialState.DISABLED: ft.icons.CLOSE,
            ft.MaterialState.DEFAULT: ft.icons.QUESTION_MARK,
        },

        track_color={
            ft.MaterialState.HOVERED: ft.colors.RED,
            ft.MaterialState.FOCUSED: ft.colors.AMBER,
            ft.MaterialState.DEFAULT: ft.colors.WHITE,
        },

        # disabled=True,
        # value=True,

        on_change=change_theme,

    )

    st2 = ft.Switch(
        label='Deseja ativar?',
        thumb_icon={
            ft.MaterialState.SELECTED: ft.icons.CHECK,
            ft.MaterialState.DISABLED: ft.icons.CLOSE,
            ft.MaterialState.DEFAULT: ft.icons.QUESTION_MARK,
        },
        on_change=change_theme,
    )

    page.add(st, st, st, st2)


if __name__ == '__main__':
    ft.app(target=main)
