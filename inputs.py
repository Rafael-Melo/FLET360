import flet as ft

def main(page: ft.Page):
    page.padding = 50
    page.scroll = ft.ScrollMode.AUTO

    page.add(
        ft.Text('TextField', style=ft.TextThemeStyle.HEADLINE_SMALL),
        ft.TextField(label='Usuário'),
        ft.TextField(label='Senha', password=True, can_reveal_password=True),
        ft.Divider(height=50),

        ft.Switch(label='Salvar dados', value=True),
        ft.Switch(label='Fechar após inatividade'),
        ft.Switch(label='Compartilhar dados', disabled=True),
        ft.Divider(height=50),

        ft.Text('Checbox', style=ft.TextThemeStyle.HEADLINE_SMALL),
        ft.Checkbox(label='Entrega rápida'),
        ft.Checkbox(label='Comida na temperatura certa'),
        ft.Checkbox(label='Entregador simpático'),
        ft.Checkbox(label='Comida saborosa'),
        ft.Divider(height=50),

        ft.Text('Dropdown', style=ft.TextThemeStyle.HEADLINE_SMALL),
        ft.Dropdown(
            label='Filtros',
            options = [
                ft.dropdown.Option(text='Próximo da sua localização'),
                ft.dropdown.Option(text='Mais bem avaliado'),
                ft.dropdown.Option(text='Aceita vale refeição'),
                ft.dropdown.Option(text='Entrega em 20 min'),
                ft.dropdown.Option(text='Com cupom'),
            ]
        ),
        ft.Divider(height=50),

        ft.Text('Slider', style=ft.TextThemeStyle.HEADLINE_SMALL),
        ft.Slider(min=0, max=100, value=10),
        ft.RangeSlider(min=0, max=100, start_value=10, end_value=50),
        ft.Divider(height=50),
    )


if __name__ == '__main__':
    ft.app(target = main, view = ft.AppView.FLET_APP)