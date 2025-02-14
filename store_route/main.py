import flet as ft
from store import Store
from home import Home

def main(page: ft.Page):
    def route_change(route):
        page.views.clear()

        if page.route == '/':
            page.views.append(
                ft.View(route='/', controls=[Home(page)])
            )

        elif page.route == '/store':
            page.views.append(
                ft.View(route='/store', controls=[Store(page)])
            )
        
        else:
            page.views.append(
                ft.View(
                    route='/404',
                    appbar=ft.AppBar(
                        title=ft.Text('404'),
                        bgcolor=ft.Colors.GREY,
                    ),
                    controls=[
                        ft.Text(value='Página não encontrada'),
                        ft.ElevatedButton(
                            text='Ir para página inicial',
                            on_click=lambda _: page.go('/')
                        )
                    ]
                )
            )
        
        page.update()
    
    page.on_route_change = route_change
    page.go(page.route)


if __name__ == '__main__':
    ft.app(target=main)
