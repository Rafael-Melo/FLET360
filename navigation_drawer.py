import flet as ft

def main(page: ft.Page):
    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Item 1",
                icon=ft.Icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.DOOR_BACK_DOOR),
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.FilledButton(text='Botão'),
                label='Item 2',
            ),
            ft.NavigationDrawerDestination(
                icon=ft.icons.PHONE_OUTLINED,
                label='Item 3',
                selected_icon=ft.icons.PHONE,
            ),
        ],
        bgcolor=ft.colors.GREY_900,
        indicator_color=ft.colors.DEEP_ORANGE,
        indicator_shape=ft.RoundedRectangleBorder(radius=10),
        selected_index=0,
        tile_padding=ft.padding.all(20),

        on_change=lambda e: print(e.control.selected_index),
    )

    def show_drawer(e):
        page.drawer.open = True
        page.drawer.update()

    btn = ft.IconButton(icon=ft.icons.MENU, on_click=show_drawer)
    page.add(btn)


if __name__ == '__main__':
    ft.app(target=main)