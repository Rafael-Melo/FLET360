import flet as ft

def main(page: ft.Page):
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.icons.HOME,
                label='Início',
            ),
            ft.NavigationBarDestination(
                label='Chat',
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label='Configurações',
            ),
            ft.NavigationBarDestination(
                icon_content=ft.Container(bgcolor='red', height=20, width=20),
                selected_icon_content=ft.Container(bgcolor='green', height=10, width=30),
                label='Início',
                tooltip='Selecione aqui'
            ),
        ],
        selected_index=0,
        indicator_color=ft.colors.WHITE,
        indicator_shape=ft.RoundedRectangleBorder(radius=5),

        on_change=lambda e: print(e.control.selected_index),

        label_behavior = ft.NavigationBarLabelBehavior.ONLY_SHOW_SELECTED,

        elevation=4,
        shadow_color=ft.colors.WHITE,
    )

    page.update()


if __name__ == '__main__':
    ft.app(target=main)