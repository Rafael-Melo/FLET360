import flet as ft

def Home(page: ft.Page):
    return ft.Container(
        bgcolor='cyan',
        height=800,
        alignment=ft.alignment.center,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text('HOME', size=40),
                ft.ElevatedButton('Ir para Loja', on_click=lambda _: page.go('/store'))
            ]
        )
    )