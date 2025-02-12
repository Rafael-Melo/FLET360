import flet as ft

def main(page: ft.Page):
    card = ft.Card(
        content=ft.Column(
            controls=[
                ft.Text(value='Título do card', style=ft.TextThemeStyle.HEADLINE_LARGE),
                ft.Text(value='Conteúdo do card', style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                ft.FilledButton(text='Salvar'),
            ]
        ),
        color=ft.Colors.GREY_900,
        elevation=5,
        margin=ft.margin.all(30),
        shadow_color=ft.Colors.WHITE,
    )

    page.add(card)


if __name__ == '__main__':
    ft.app(target=main)