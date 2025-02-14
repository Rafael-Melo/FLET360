import flet as ft

def main(page: ft.Page):
    page.spacing = 50

    # theme = ft.Theme(
    #     color_scheme=ft.ColorScheme(
    #         primary=ft.colors.PURPLE,
    #         secondary=ft.colors.CYAN,
    #     ),
    #     text_theme=ft.TextTheme(
    #         title_large=ft.TextStyle(size=50, weight=ft.FontWeight.W_900)
    #     )
    # )

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.PURPLE,
            secondary=ft.colors.CYAN,
        ),
        text_theme=ft.TextTheme(
            title_large=ft.TextStyle(size=50, weight=ft.FontWeight.W_900)
        )
    )
    
    page.add(
        ft.Container(
            height=100,
            width=200,
            padding=10,
            content=ft.Column(
                controls=[
                    ft.Text(value='Título', style=ft.TextThemeStyle.TITLE_LARGE),
                    ft.ElevatedButton(text='Botão', color=ft.colors.AMBER),
                    ft.FilledButton(text='Botão Primário'),
                ]
            ),
            bgcolor=ft.colors.PRIMARY
        )
    )

    page.add(
        ft.Container(
            height=100,
            width=200,
            padding=10,
            content=ft.Column(
                controls=[
                    ft.Text(value='Título', style=ft.TextThemeStyle.TITLE_LARGE),
                    ft.ElevatedButton(text='Botão', color=ft.colors.AMBER),
                    ft.FilledButton(text='Botão Primário'),
                ]
            ),
            bgcolor=ft.colors.PRIMARY,
            # theme=theme
        )
    )

    page.theme_mode = ft.ThemeMode.LIGHT
    tema = ft.Text()

    def change_theme(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            tema.value = 'Tema Light'
        else:
            page.theme_mode = ft.ThemeMode.DARK
            tema.value = 'Tema Dark'
        page.update()


    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.CHANGE_CIRCLE, on_click=change_theme,
    )

    page.add(tema)


if __name__ == '__main__':
    ft.app(target=main)