import flet as ft

def main(page: ft.Page):
    def route_change(route):
        troute = ft.TemplateRoute(page.route)

        if troute.match('/loja/:produto'):
            page.add(
                ft.Text(
                    value=f'Acessando página do produto: {troute.produto}'
                )
            )
        elif troute.match('/loja/:produto/pedido/:id'):
            page.add(
                ft.Text(
                    value=f'Acessando página de compra do produto: {troute.produto}, com id: {troute.id}, {troute.id.isnumeric()}'
                )
            )
        else:
            page.add(ft.Text(value='Página não encontrada'))
    
    page.on_route_change = route_change
    page.update()


if __name__ == '__main__':
    ft.app(target=main)