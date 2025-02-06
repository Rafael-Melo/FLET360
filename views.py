import flet as ft

def main(page: ft.Page):
    page.title = 'Rotas'

    def change_route(e):
        match e.control.selected_index:
            case 0:
                page.go('/')
            case 1:
                page.go('/loja')
            case 2:
                page.go('/usuario')

        # if e.control.selected_index == 0:
        #     page.go('/')
        # elif e.control.selected_index == 1:
        #     page.go('/loja')
        # elif e.control.selected_index == 2:
        #     page.go('/usuario')


    def route_change(route):
        page.views.clear()

        if page.route=='/':
            page.views.append(
                ft.View(
                    route="/",
                    appbar=ft.AppBar(
                        title=ft.Text('Meu App'),
                        bgcolor=ft.Colors.GREY,
                    ),
                    controls=[
                        ft.ElevatedButton(
                            text='Ver loja',
                            on_click=lambda _: page.go('/loja'),
                        ),
                        ft.ListView(
                            controls=[
                                ft.Text(
                                    value=f'Item {i}',
                                    size=30
                                ) for i in range(50)
                            ]
                        )
                    ],
                    scroll=ft.ScrollMode.AUTO,
                    auto_scroll=False,
                    bgcolor=ft.Colors.BLACK,
                    drawer=ft.NavigationDrawer(
                        controls=[
                            ft.NavigationDrawerDestination(
                                label='Home',
                                icon=ft.Icons.HOME,
                            ),
                            ft.NavigationDrawerDestination(
                                label='Loja',
                                icon=ft.Icons.STORE,
                            ),
                            ft.NavigationDrawerDestination(
                                label='Usuário',
                                icon=ft.Icons.MANAGE_ACCOUNTS,
                            ),
                        ],
                        on_change=change_route,
                    ),
                    end_drawer=ft.NavigationDrawer(
                        controls=[
                            ft.NavigationDrawerDestination(label='Configurações'),
                            ft.NavigationDrawerDestination(label='Dados da Conta'),
                            ft.NavigationDrawerDestination(label='Sair'),
                        ]
                    ),
                    floating_action_button=ft.FloatingActionButton(icon=ft.Icons.ADD),
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.START,
                    padding=ft.padding.all(20),
                )
            )

        elif page.route == '/loja':
            page.views.append(
                ft.View(
                    route='/loja',
                    appbar=ft.AppBar(
                        title=ft.Text('Loja'),
                        bgcolor=ft.Colors.GREY,
                    ),
                    controls=[
                        ft.ElevatedButton(
                            text='Ir para página inicial',
                            on_click=lambda _: page.go('/')
                        ),
                        ft.ElevatedButton(
                            text='Ir para página do usuário',
                            on_click=lambda _: page.go('/usuario')
                        )
                    ],
                    fullscreen_dialog=False,
                )
            )

        elif page.route == '/usuario':
            page.views.append(
                ft.View(
                    route='/usuario',
                    appbar=ft.AppBar(
                        title=ft.Text('Usuário'),
                        bgcolor=ft.Colors.GREY,
                    ),
                    controls=[
                        ft.ElevatedButton(
                            text='Ir para página inicial',
                            on_click=lambda _: page.go('/')
                        )
                    ]
                )
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

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)    
    
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == '__main__':
    ft.app(target=main)