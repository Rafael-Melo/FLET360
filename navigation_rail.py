import flet as ft

def main(page: ft.Page):
    rail = ft.NavigationRail(
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.HOME,
                label='Início',
            ),
            ft.NavigationRailDestination(
                label='Chat',
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label='Itens Salvos',
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Container(bgcolor='red', height=20, width=20),
                selected_icon_content=ft.Container(bgcolor='green', height=10, width=30),
                # label='Configurações',
                label_content=ft.Text(value='Configurações', size=20, weight=ft.FontWeight.BOLD),
                padding=ft.padding.only(top=50),
            ),
        ],
        bgcolor=ft.colors.GREY_900,
        selected_index=0,
        extended=True,
        # min_width=200,
        # min_extended_width=200,
        trailing=ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(text="Cadastrar novo"),
                ft.PopupMenuItem(text="Enviar em massa"),
            ]
        ),
        leading=ft.CircleAvatar(content=ft.Text(value='RM')),
        on_change=lambda e: print(e.control.selected_index),
    )

    row = ft.Row(controls=[rail], expand=True)
    page.add(row)


if __name__ == '__main__':
    ft.app(target=main)
