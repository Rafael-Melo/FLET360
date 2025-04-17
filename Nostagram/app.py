import flet as ft
from main import main_view
from detail import detail_view

def app_routes(page: ft.Page):
    def route_change(e):
        page.views.clear()

        if page.route == "/":
            page.views.append(main_view(page))
        elif page.route.startswith("/detail/"):
            page.views.append(detail_view(page))

        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=app_routes, assets_dir="../assets")
