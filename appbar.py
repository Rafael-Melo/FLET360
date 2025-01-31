import flet as ft

def main(page: ft.Page):
    page.appbar = ft.AppBar(
        bgcolor=ft.colors.BLACK,
        title=ft.Text(value='App Fit'),
        center_title=False,
        toolbar_height=100,
        color=ft.colors.GREEN,
        leading=ft.Icon(name=ft.icons.HOME),
        leading_width=100,
        actions=[
            ft.IconButton(icon=ft.icons.SUNNY),
            ft.IconButton(icon=ft.icons.NOTIFICATIONS),
            ft.CircleAvatar(content=ft.Text(value='RM')),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text='Meus Dados'),
                    ft.PopupMenuItem(text='Configurações'),
                    ft.PopupMenuItem(text='Sair'),
                ]
            )
        ]
    )

    page.update()


if __name__ == '__main__':
    ft.app(target=main)
