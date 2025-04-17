import flet as ft

local = {'0':'Cidade República','1':'Templo do Ar do Sul','2':'Tribo da água do Sul','3':'Algum lugar do céu','4':'Templo do Ar do Sul','5':'Reino da Terra','6':'Ba Sing Se','7':'Omashu','8':'Caverna dos Mestres','9':'Mundo Fspiritual','10':'Reino do Fogo','11':'Fim do Mundo',}
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
legenda = {'0': 'Reencontrando o Time Avatar para inauguração da Cidade República 📌🏛', '1': 'Eu 😁', '2': 'Novos amigos!!', '3':'Appa', '4':'Ele vai chamar Momo 🙊', '5':'Shopping!!', '6':'War is coming', '7':'A maior dobradora de terra do mundo, Toph!', '8':'Quem diria que seu maior inimigo poderia se tornar seu melhor amigo', '9':'iroh é uma das pessoas mais sábeis e gentis que já conheci', '10':'Nós', '11':'Sempre há escolhas'}

def detail_view(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    img_id = page.route.split("/")[-1]

    def clicked(e):
        e.control.selected = not e.control.selected
        e.control.update()

    layout = ft.Container(
        bgcolor=ft.Colors.WHITE,
        width=500,
        border_radius=ft.border_radius.all(10),
        shadow=ft.BoxShadow(blur_radius=50, color=ft.Colors.TEAL),
        content=ft.Column(
            spacing=0,
            controls=[
                ft.ListTile(
                    title=ft.Text(value='Avatar', color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                    subtitle=ft.Text(value=f'{local[img_id]}', color=ft.Colors.BLACK),
                    leading=ft.Image(
                        src='images/Avatar.png',
                        fit=ft.ImageFit.CONTAIN,
                        border_radius=ft.border_radius.all(30)
                    ),
                    trailing=ft.IconButton(
                        icon=ft.Icons.ARROW_BACK,
                        icon_color=ft.Colors.BLACK,
                        on_click=lambda e: page.go("/"),
                    )
                ),
                ft.Image(
                    src=f'images/Nostagram{img_id}.png',
                    fit=ft.ImageFit.FILL,
                ),
                ft.Container(
                    padding=ft.padding.all(15),
                    content=ft.Column(
                        controls=[
                            ft.ResponsiveRow(
                                columns=12,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.IconButton(
                                        col=1,
                                        icon=ft.Icons.FAVORITE_BORDER,
                                        icon_color=ft.Colors.BLACK,
                                        selected_icon=ft.Icons.FAVORITE,
                                        selected_icon_color=ft.Colors.RED,
                                        selected=False,
                                        on_click=clicked,
                                    ),
                                    ft.Icon(
                                        col=1,
                                        name=ft.Icons.CHAT_BUBBLE_OUTLINE,
                                        color=ft.Colors.BLACK,
                                    ),
                                    ft.Icon(
                                        col=1,
                                        name=ft.Icons.SEND,
                                        color=ft.Colors.BLACK,
                                    ),
                                    ft.Container(col=8),
                                    ft.IconButton(
                                        col=1,
                                        icon=ft.Icons.BOOKMARK_BORDER,
                                        icon_color=ft.Colors.BLACK,
                                        selected_icon=ft.Icons.BOOKMARK_ROUNDED,
                                        selected_icon_color=ft.Colors.BLACK,
                                        selected=False,
                                        on_click=clicked,
                                    ),
                                ]
                            ),
                            ft.Text(
                                spans=[
                                    ft.TextSpan(
                                        text='Curtido por ',
                                        style=ft.TextStyle(color=ft.Colors.BLACK, size=16)
                                    ),
                                    ft.TextSpan(
                                        text='rafamelo7 ',
                                        style=ft.TextStyle(color=ft.Colors.BLACK, size=16, weight=ft.FontWeight.BOLD)
                                    ),
                                    ft.TextSpan(
                                        text='e ',
                                        style=ft.TextStyle(color=ft.Colors.BLACK, size=16)
                                    ),
                                    ft.TextSpan(
                                        text='2985 outros',
                                        style=ft.TextStyle(color=ft.Colors.BLACK, size=16, weight=ft.FontWeight.BOLD)
                                    ),
                                ]
                            ),
                            ft.Text(
                                value=f'{legenda[img_id]}',
                                color=ft.Colors.BLACK,
                                size=16,
                            ),
                            ft.Text(
                                value='1023 ANOS ATRÁS',
                                color=ft.colors.GREY,
                                size=14,
                                offset=ft.Offset(x=0, y=-0.5),
                            ),
                            ft.Text(
                                spans=[
                                    ft.TextSpan(
                                        text='Sokka ',
                                        style=ft.TextStyle(color=ft.Colors.BLACK, size=16, weight=ft.FontWeight.BOLD)
                                    ),
                                    ft.TextSpan(
                                        text='Pra sempre #TimeBoomerang!',
                                        style=ft.TextStyle(color=ft.Colors.BLACK, size=16)
                                    ),
                                ]
                            ),
                            ft.Text(
                                spans=[
                                    ft.TextSpan(
                                        text='Toph ',
                                        style=ft.TextStyle(color=ft.Colors.BLACK, size=16, weight=ft.FontWeight.BOLD)
                                    ),
                                    ft.TextSpan(
                                        text='Eu não vi isso...',
                                        style=ft.TextStyle(color=ft.Colors.BLACK, size=16)
                                    ),
                                ]
                            ),
                            ft.Text(
                                value='Ver todos os 3627 comentários',
                                color=ft.colors.GREY,
                                size=16,
                            ),
                            ft.TextField(
                                hint_text='Adicione um comentário...',
                                hint_style=ft.TextStyle(color=ft.Colors.GREY, size=16),
                                border=ft.InputBorder.UNDERLINE,
                                border_color=ft.Colors.GREY,
                                border_width=1,
                                color=ft.Colors.BLACK,
                            )
                        ]
                    )
                )
            ]
        )
    )

    layout = ft.View(
        route=page.route,
        controls=[
            ft.Container(
                alignment=ft.alignment.center,
                content=ft.Column(
                    controls=[layout]
                )
            )
        ]
    )

    return layout