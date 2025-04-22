import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 0

    bg = ft.Image(
        src='https://images3.alphacoders.com/133/1332803.png',
        fit=ft.ImageFit.COVER,
    )

    tx = ft.Container(
        padding=ft.padding.symmetric(vertical=50, horizontal=80),
        border_radius=ft.border_radius.all(10),
        bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
        border=ft.Border(
            top=ft.BorderSide(width=2, color=ft.Colors.WHITE30),
            right=ft.BorderSide(width=2, color=ft.Colors.WHITE30)
        ),
        blur=ft.Blur(sigma_x=8, sigma_y=8),
        content=(
            ft.Text(
                value='RAFA PROGRAMADOR',
                size=40,
                color=ft.Colors.WHITE,
            )
        ),
        width=600,
        alignment=ft.alignment.center
    )

    stack = ft.Stack(
        controls=[
            bg,
            tx,
        ],
        alignment=ft.alignment.center
    )

    page.add(stack)

if __name__ == '__main__':
    ft.app(target=main)