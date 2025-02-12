import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Column(
            spacing=0,
            expand=True,
            controls=[
                ft.Container(
                    bgcolor=ft.Colors.CYAN_100,
                    expand=True,
                ),
                ft.Divider(),
                ft.Container(
                    bgcolor=ft.Colors.BLUE,
                    expand=True,
                ),
                ft.Divider(
                    height=1,
                    color=ft.Colors.WHITE,
                ),
                ft.Container(
                    bgcolor=ft.Colors.DEEP_PURPLE,
                    expand=True,
                ),
                ft.Divider(
                    height=50,
                    thickness=10,
                    color=ft.Colors.INDIGO,
                ),
                ft.Container(
                    bgcolor=ft.Colors.GREEN_ACCENT,
                    expand=True,
                ),
            ]
        )
    )


if __name__ == '__main__':
    ft.app(target=main)