import flet as ft

# def main(page: ft.Page):
#     page.add(ft.Text(f'Página inicial', size= 40))
#     def route_change(e: ft.RouteChangeEvent):
#         page.add(ft.Text(f'Acesando: {e.route}', size=40))
#         page.on_route_change = route_change
#     page.add(
#         ft.ElevatedButton(
#             text='Ir para loja',
#             on_click=lambda _: page.go('/loja')
#         )
#     )
#     page.add(
#         ft.ElevatedButton(
#             text='Ir para home',
#             on_click=lambda _: page.go('/home')
#         )
#     )
#     page.add(
#         ft.ElevatedButton(
#             text='Ir para minhas compras',
#             on_click=lambda _: page.go('/minhas-compras')
#         )
#     )


# if __name__ == '__main__':
#     ft.app(target=main)

def main(page: ft.Page):
    page.add(ft.Text(f"Initial route: {page.route}"))

    def route_change(e: ft.RouteChangeEvent):
        page.add(ft.Text(f"New route: {e.route}"))

    page.on_route_change = route_change
    page.update()

ft.app(main, view=ft.AppView.WEB_BROWSER)

# Caminho para executar na web
# flet run .\views_exemplos.py -w
# ft.app(main, view=ft.AppView.WEB_BROWSER)