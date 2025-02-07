import flet as ft

def Store(page: ft.Page):
    return ft.Container(
        bgcolor='amber',
        height=800,
        alignment=ft.alignment.center,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text('STORE', size=40),
                ft.ElevatedButton('Voltar para Home', on_click=lambda _: page.go('/'))
            ]
        )
    )
