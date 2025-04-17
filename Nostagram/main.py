import flet as ft

def main_view(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.scroll = ft.ScrollMode.HIDDEN
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_title_bar_hidden = True

    def follow(e):
        e.control.content.value = 'Seguindo'
        e.control.content.color = ft.colors.BLACK
        e.control.bgcolor = ft.colors.GREY_300
        e.control.update()

    def show_image_detail(e):
        img_num = e.control.data
        print(f'Imagem clicada: {img_num}')
        e.page.go(f"/detail/{img_num}")

    header = ft.Container(
        padding=ft.padding.all(20),
        content=ft.ResponsiveRow(
            columns=12,
            controls=[
                ft.Container(
                    col={'xs':12, 'sm':4},
                    padding=40,
                    bgcolor=ft.colors.BLACK,
                    shape=ft.BoxShape.CIRCLE,
                    shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.LIGHT_BLUE),
                    height=200,
                    content=ft.Image(
                        src='images/Avatar.png',
                    ),
                ),
                ft.Container(
                    col={'xs':12, 'sm':8},
                    content=ft.ResponsiveRow(
                        columns=12,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        run_spacing=20,
                        controls=[
                            ft.Row(
                                col=11,
                                controls=[
                                    ft.Text(
                                        value='avatardeveloper',
                                        color=ft.colors.BLUE,
                                        size=24,
                                    ),
                                    ft.Icon(
                                        name=ft.icons.VERIFIED,
                                        color=ft.colors.BLUE_500,
                                        size=20,
                                    )
                                ]
                            ),
                            ft.Icon(
                                col=1,
                                name=ft.icons.MORE_HORIZ,
                                color=ft.colors.WHITE,
                            ),
                            ft.Container(
                                col=4,
                                bgcolor=ft.colors.BLUE_500,
                                content=ft.Text(
                                    value='Seguir',
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.colors.WHITE,
                                ),
                                border_radius=ft.border_radius.all(10),
                                padding=ft.padding.symmetric(
                                    vertical=5,
                                    horizontal=10
                                ),
                                alignment=ft.alignment.center,
                                on_click=follow,
                            ),
                            ft.Container(
                                col=6,
                                bgcolor=ft.colors.GREY_300,
                                content=ft.Text(
                                    value='Enviar Mensagem',
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.colors.BLACK,
                                    max_lines=1,
                                    overflow=ft.TextOverflow.ELLIPSIS,
                                ),
                                border_radius=ft.border_radius.all(10),
                                padding=ft.padding.symmetric(
                                    vertical=5,
                                    horizontal=10
                                ),
                                alignment=ft.alignment.center,
                            ),
                            ft.Text(
                                col={'xs':12, 'sm':4},
                                spans=[
                                    ft.TextSpan(
                                        text='139 ',
                                        style=ft.TextStyle(
                                            color=ft.colors.WHITE,
                                            weight=ft.FontWeight.BOLD,
                                        )
                                    ),
                                    ft.TextSpan(
                                        text='publicações',
                                        style=ft.TextStyle(
                                            color=ft.colors.WHITE,
                                        )
                                    ),
                                ]
                            ),
                            ft.Text(
                                col={'xs':12, 'sm':4},
                                spans=[
                                    ft.TextSpan(
                                        text='100 mil ',
                                        style=ft.TextStyle(
                                            color=ft.colors.WHITE,
                                            weight=ft.FontWeight.BOLD,
                                        )
                                    ),
                                    ft.TextSpan(
                                        text='seguidores',
                                        style=ft.TextStyle(
                                            color=ft.colors.WHITE,
                                        )
                                    ),
                                ]
                            ),
                            ft.Text(
                                col={'xs':12, 'sm':4},
                                spans=[
                                    ft.TextSpan(
                                        text='133 ',
                                        style=ft.TextStyle(
                                            color=ft.colors.WHITE,
                                            weight=ft.FontWeight.BOLD,
                                        )
                                    ),
                                    ft.TextSpan(
                                        text='seguindo',
                                        style=ft.TextStyle(
                                            color=ft.colors.WHITE,
                                        )
                                    ),
                                ]
                            ),
                            ft.Text(
                                col=12,
                                value='Avatar Developer',
                                color=ft.colors.WHITE,
                                weight=ft.FontWeight.BOLD,
                            ),
                            ft.Text(
                                col=12,
                                color=ft.colors.WHITE,
                                spans=[
                                    ft.TextSpan(text='Teaching programming from the ground up! 🤯\n'),
                                    ft.TextSpan(text='Follow on YouTube: Avatar Developer ▶️\n'),
                                    ft.TextSpan(text='Free courses in Python, SQL, Django, and more in the link  👇👇👇\n'),
                                    ft.TextSpan(
                                        text='🔗 linktr.ee/avatardeveloper',
                                        url='https://linktr.ee/avatardeveloper',
                                        style=ft.TextStyle(
                                            color=ft.colors.BLUE,
                                        )
                                        ),
                                ]
                            ),
                            ft.Text(
                                spans=[
                                    ft.TextSpan(
                                        text='Seguido por ',
                                        style=ft.TextStyle(
                                            color=ft.colors.GREY_700,
                                        )
                                    ),
                                    ft.TextSpan(
                                        text='você ',
                                        style=ft.TextStyle(
                                            color=ft.colors.GREY,
                                            weight=ft.FontWeight.BOLD,
                                        )
                                    ),
                                    ft.TextSpan(
                                        text='e outras 100 pessoas',
                                        style=ft.TextStyle(
                                            color=ft.colors.GREY_700,
                                        ),
                                    ),
                                ],
                                size=14,
                            )
                        ]
                    )
                )
            ]
        )
    )

    stories = ft.Container(
        padding=ft.padding.all(20),
        content=ft.Row(
            scroll=ft.ScrollMode.HIDDEN,
            controls=[
                ft.Image(
                    src=f'https://picsum.photos/150/150?{num}',
                    border_radius=ft.border_radius.all(100),
                    width=100,
                ) for num in range(15)
            ]
        )
    )

    grid = ft.GridView(
        runs_count=3,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
        controls=[
            ft.Container(
                data=num,
                on_click=show_image_detail,
                content=ft.Image(
                    src=f'images/Nostagram{num}.png',
                    fit=ft.ImageFit.COVER,
                )
            ) for num in range(12)
        ]
    )

    posts = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        label_color=ft.colors.WHITE,
        unselected_label_color=ft.colors.GREY,
        divider_color=ft.colors.BLACK,
        indicator_color=ft.colors.GREY,
        scrollable=False,
        tabs=[
            ft.Tab(
                icon=ft.icons.GRID_ON,
                text='PUBLICAÇÕES',
                content=grid,
            ),
            ft.Tab(
                icon=ft.icons.VIDEO_COLLECTION_OUTLINED,
                text='REELS',
                content=grid,
            ),
            ft.Tab(
                icon=ft.icons.BOOKMARK_BORDER,
                text='SALVOS',
                content=grid,
            ),
        ]
    )

    layout = ft.View(
        route="/",
        controls=[
            ft.Container(
                width=900,
                content=ft.Column(
                    spacing=0,
                    controls=[
                        header,
                        stories,
                        ft.Divider(color=ft.colors.GREY),
                        posts,
                    ]
                )
            )
        ]
    )

    return layout