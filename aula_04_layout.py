import flet as ft
import math

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    st = ft.Stack(
        controls=[
            ft.Container(
                content=ft.Image(
                    src='https://wallpapers.com/images/featured/open-world-games-ew2yvrmjn6q38krq.jpg',
                    fit=ft.ImageFit.COVER,
                ),
                expand=True,
            ),
            ft.Container(
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                    colors=[ft.colors.TEAL, ft.colors.BLUE]
                ),
                opacity=0.3,
                expand=True,
            ),
            ft.Container(
                content=ft.Image(
                    src='images/fire-dragon.png'
                ),
            ),
            ft.Text(value='Dragão!', color=ft.colors.GREY, style=ft.TextThemeStyle.HEADLINE_LARGE),
            ft.Column(
                controls=[
                    ft.Text(value='Curso de Cavaleiro', style=ft.TextThemeStyle.HEADLINE_LARGE),
                    ft.Text(value='Aprenda todos os conceitos e cace seus próprios Dragões com honra!', style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                    ft.FilledButton(text='Saiba mais'),
                ]
            ),
        ],
        expand=True,
        alignment=ft.alignment.center,
    )

    row1 = ft.Row(
        controls=[
            ft.ElevatedButton(
                text='Bt 01',
                bgcolor=ft.colors.BLUE,
                color=ft.colors.WHITE,
            ),
            ft.ElevatedButton(
                text='Bt 02',
                bgcolor=ft.colors.BLUE,
                color=ft.colors.WHITE,
            ),
            ft.ElevatedButton(
                text='Bt 03',
                bgcolor=ft.colors.BLUE,
                color=ft.colors.WHITE,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        spacing=0, # Espaço entre os objetos horizontalmente
        wrap=True, # Quebra de linha
        run_spacing=30, # Espaço entre os objetos verticalmente
    )

    row2 = ft.Row(
        controls=[
            ft.Image(height=200, src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYZqZkpMyiN2uSuT7GAf6JSkJ44YsZqoQHdw&s'),
            ft.Image(height=200, src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxvblcNgMEtxyTOs9HfZGhaaOXhG7cyrF9UQ&s'),
            ft.Image(height=200, src='https://www.unite.ai/wp-content/uploads/2022/04/AI-Python-Libraries.png'),
            ft.Image(height=200, src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5qn-GuWwc6EFc-xcy9haXoDY0YoVZEgwQ8Q&s'),
            ft.Image(height=200, src='https://www.forbes.com/advisor/wp-content/uploads/2023/06/python-coding-graphic.jpeg.jpg'),
        ],
        scroll=ft.ScrollMode.AUTO,
        auto_scroll=True,
    )

    rrow1 = ft.ResponsiveRow(
        columns=12,
        run_spacing=50,
        spacing=20,
        controls=[
            ft.ElevatedButton(
                col={'sm': 4, 'md': 3, 'lg': 2, 'xl': 1},
                text='Bt 01',
                bgcolor=ft.colors.AMBER,
                color=ft.colors.BLACK,
            ),
            ft.ElevatedButton(
                col={'sm': 4, 'md': 3, 'lg': 2, 'xl': 1},
                text='Bt 02',
                bgcolor=ft.colors.AMBER,
                color=ft.colors.BLACK,
            ),
            ft.ElevatedButton(
                col={'sm': 4, 'md': 3, 'lg': 2, 'xl': 1},
                text='Bt 03',
                bgcolor=ft.colors.AMBER,
                color=ft.colors.BLACK,
            ),
            ft.ElevatedButton(
                col={'sm': 4, 'md': 3, 'lg': 6},
                text='Bt 01',
                bgcolor=ft.colors.RED,
                color=ft.colors.GREEN_400,
            ),
            ft.ElevatedButton(
                col={'sm': 4, 'md': 3, 'lg': 6},
                text='Bt 02',
                bgcolor=ft.colors.RED,
                color=ft.colors.GREEN_400,
            ),
            ft.ElevatedButton(
                col={'sm': 4, 'md': 3, 'lg': 6},
                text='Bt 03',
                bgcolor=ft.colors.RED,
                color=ft.colors.GREEN_400,
            ),
        ]
    )

    # size_text = ft.Text()

    # def page_size(e):
    #     size_text.value = f'Largura: {page.window.width} x Altura: {page.window.height}'
    #     size_text.update()

    # page.on_resized = page_size

    # page.add(st, row1, row2, rrow1, size_text)

    col1 = ft.Column(
        controls=[
            ft.ElevatedButton(text='BT01', bgcolor=ft.colors.GREEN, color=ft.colors.WHITE),
            ft.ElevatedButton(text='BT02', bgcolor=ft.colors.GREEN, color=ft.colors.WHITE),
            ft.ElevatedButton(text='BT03', bgcolor=ft.colors.GREEN, color=ft.colors.WHITE),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=20,
        wrap=False,
        run_spacing=50,
        width=500,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )

    # page.add(ft.Container(col1, bgcolor=ft.colors.GREY))

    container = ft.Container(
        # content=ft.Image(
        #     src='https://flet.dev/img/docs/controls/container/container-diagram.png'
        # ),
        # height=100,
        # width=200,
        image_src='https://flet.dev/img/docs/controls/container/container-diagram.png',
        margin=ft.margin.all(10),
        border=ft.border.all(width=10, color=ft.colors.INDIGO),
        border_radius=ft.border_radius.all(10),
        expand=True,
        bgcolor=ft.colors.WHITE,
        alignment=ft.alignment.center,
        padding=ft.padding.all(30),
        shape=ft.BoxShape.CIRCLE,
        shadow=[
            ft.BoxShadow(
            # spread_radius=10,
            blur_radius=30,
            color=ft.colors.DEEP_ORANGE,
            blur_style=ft.ShadowBlurStyle.NORMAL,
            offset=ft.Offset(x=50, y=40)
            ),
            ft.BoxShadow(
            # spread_radius=10,
            blur_radius=0,
            color=ft.colors.GREEN,
            blur_style=ft.ShadowBlurStyle.NORMAL,
            offset=ft.Offset(x=-50, y=-40)
            ),
        ],
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[ft.colors.PURPLE, ft.colors.LIGHT_BLUE],
        ),
        content=ft.Row(
            controls=[
                ft.ElevatedButton(text='Texto 1'),
                ft.ElevatedButton(text='Texto 2'),
                ft.ElevatedButton(text='Texto 3'),
                ft.ElevatedButton(text='Texto 4'),

            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    # page.add(container)

    # Aspect Ratio:
    # 9:16  -> 0.56
    # 2:3   -> 0.66
    # 1:1   -> 1.0
    # 16:8  -> 1.77
    # page.add(ft.Image(src='https://image-processor-storage.s3.us-west-2.amazonaws.com/uploads/2f8564029850db041025d8d45865e617/view-of-pair-walking-in-watermaldives.jpeg'))

    grid = ft.GridView(
        controls=[
            ft.Image(src=f'https://picsum.photos/250/300?{num}', fit='cover') for num in range(20)
        ],
        runs_count=3, # Três elementos independente do tamanho
        padding=10,
        spacing=10,
        run_spacing=10,
        # max_extent= 100, # Largura máxima de 100 pra cada elemento idependente da quantidade
        expand=True,
        # height=300,
        # width=300,
        auto_scroll=True,
        child_aspect_ratio=1.77,
    )

    # page.add(grid)

    containers = [
        # ft.Container(height=100, width=200, bgcolor=ft.colors.DEEP_ORANGE),
        # ft.Container(height=100, width=200, bgcolor='deeporange'),
        # ft.Container(height=100, width=200, bgcolor='deeporange,0.5'),
        # ft.Container(height=100, width=200, bgcolor='#FC6225'),
        # ft.Container(height=100, width=200, bgcolor='#7FFC6225'), # 00 - FF 2 digitos antes do padrão hex definem a opacidade
        # ft.Container(height=100, width=200, bgcolor=ft.colors.with_opacity(0.5, ft.colors.DEEP_ORANGE)),
        # ft.Container(height=100, width=200, bgcolor=ft.colors.with_opacity(0.2, 'deeporange')),
        # ft.Container(height=100, width=200, bgcolor=ft.colors.with_opacity(0.9, '#FC6225')),
        ft.Container(
            expand=True,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=[ft.colors.AMBER, ft.colors.RED, ft.colors.PURPLE],
                stops= [0, 0.7, 1],
                rotation=math.radians(45), # inclinação do gadiente em graus.
            )
        ),
        ft.Container(
            expand=True,
            gradient=ft.RadialGradient(
                colors=[ft.colors.CYAN, ft.colors.BLUE, ft.colors.PURPLE],
                stops= [0, 0.5, 1],
                center=ft.Alignment(x=-0.5, y=-0.5),
                radius=1,
            )
        ),
        ft.Container(
            expand=True,
            gradient=ft.SweepGradient(
                colors=[ft.colors.GREEN, ft.colors.BLACK, ft.colors.GREEN],
                stops= [0, 0.5, 1],
                center=ft.Alignment(x=0, y=0),
                rotation=math.radians(310),
            )
        ),
    ]

    page.add(*containers)


ft.app(target=main, assets_dir='assets')
