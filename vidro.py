import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 0

    # Imagem de fundo (expandida para ocupar toda a tela)
    bg = ft.Image(
        src='https://images3.alphacoders.com/133/1332803.png',
        fit=ft.ImageFit.COVER,
        expand=True
    )

    # Título e subtítulo
    nome = ft.Text(
        value='<SISTEMA',
        size=30,
        color=ft.Colors.WHITE,
        weight=ft.FontWeight.BOLD,
    )

    subtitulo = ft.Text(
        value='           DEV/>',
        size=30,
        color=ft.Colors.PURPLE,
        weight=ft.FontWeight.BOLD,
    )

    # Avatar
    logo = ft.Image(
        src='https://static.vecteezy.com/system/resources/thumbnails/048/216/761/small/modern-male-avatar-with-black-hair-and-hoodie-illustration-free-png.png',
        height=70,
    )

    # Container com os elementos do formulário
    tx = ft.Container(
        padding=ft.padding.symmetric(vertical=50, horizontal=80),
        border_radius=ft.border_radius.all(10),
        bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
        border=ft.Border(
            top=ft.BorderSide(width=2, color=ft.Colors.WHITE30),
            right=ft.BorderSide(width=2, color=ft.Colors.WHITE30)
        ),
        blur=ft.Blur(sigma_x=8, sigma_y=8),
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Container(content=nome, padding=0),
                                ft.Container(content=subtitulo, padding=0),
                            ],
                            spacing=-15,
                            alignment=ft.alignment.center
                        ),
                        logo,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                ft.TextField(
                    label='Usuário',
                    hint_text='Digite seu nome de usuário',
                    bgcolor=ft.Colors.with_opacity(0.3, ft.Colors.WHITE),
                    border_color=None
                ),
                ft.TextField(
                    label='Senha',
                    hint_text='Digite sua senha',
                    password=True,
                    can_reveal_password=True,
                    bgcolor=ft.Colors.with_opacity(0.3, ft.Colors.WHITE),
                    border_color=None
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text='Login',
                            height=50,
                            color=ft.Colors.WHITE,
                            bgcolor=ft.Colors.INDIGO_900,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                            ),
                            expand=True
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True
        ),
        width=600,
        alignment=ft.alignment.center
    )

    # Stack com fundo e formulário
    stack = ft.Stack(
        controls=[bg, tx],
        alignment=ft.alignment.center
    )

    page.add(stack)

if __name__ == '__main__':
    ft.app(target=main)
