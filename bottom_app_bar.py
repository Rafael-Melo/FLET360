import flet as ft

def main(page: ft.Page):
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.BLUE,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE),
                # ft.Container(expand=True, bgcolor=ft.colors.AMBER),
                ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
                ft.IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )
    )

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD,
    )

    page.update()


if __name__ == '__main__':
    ft.app(target=main)
