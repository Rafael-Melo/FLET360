import flet as ft

def main(page: ft.Page):
    layout = ft.Container(
        bgcolor=ft.Colors.GREY_800,
        padding=ft.padding.all(20),
        content=ft.Row(
            controls=[
                ft.Container(
                    bgcolor=ft.Colors.RED,
                    padding=ft.padding.all(20),
                    content=ft.Icon(name=ft.icons.ABC, size=30),
                ),
                ft.Container(
                    bgcolor=ft.Colors.CYAN,
                    padding=ft.padding.all(20),
                    content=ft.Column(
                        controls=[
                            ft.Text(value='Título do elemento', weight=ft.FontWeight.BOLD),
                            ft.Text(value='Conteúdo do elemento informativo'),
                        ]
                    ),
                ),
            ]
        )
    )

    page.add(layout)

    layout.content.controls[0].content.name = ft.icons.PHONE
    # layout.content.controls[0].content.update()

    layout.content.controls[1].content.controls[0].value = 'Novo título'
    layout.content.update()

    icone_componente = ft.Ref[ft.Icon]()
    titulo_componente = ft.Ref[ft.Text]()

    layout = ft.Container(
        bgcolor=ft.Colors.GREY_800,
        padding=ft.padding.all(20),
        content=ft.Row(
            controls=[
                ft.Container(
                    bgcolor=ft.Colors.RED,
                    padding=ft.padding.all(20),
                    content=ft.Icon(ref=icone_componente, name=ft.icons.ABC, size=30),
                ),
                ft.Container(
                    bgcolor=ft.Colors.CYAN,
                    padding=ft.padding.all(20),
                    content=ft.Column(
                        controls=[
                            ft.Text(ref=titulo_componente, value='Título do elemento', weight=ft.FontWeight.BOLD),
                            ft.Text(value='Conteúdo do elemento informativo'),
                        ]
                    ),
                ),
            ]
        )
    )

    page.add(layout)

    icone_componente.current.name = ft.Icons.PHONE
    icone_componente.current.update()

    titulo_componente.current.value = 'Novo titulo'
    titulo_componente.current.update()


if __name__ == '__main__':
    ft.app(target=main)