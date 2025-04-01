import flet as ft

def main(page: ft.Page):
    layout = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.ShaderMask(
                        content=ft.Text(value='Rafael Melo', size=100),
                        shader=ft.LinearGradient(
                            colors=[ft.Colors.DEEP_PURPLE, ft.Colors.PINK, ft.Colors.CYAN],
                        )
                    ),
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.ShaderMask(
                                content=ft.Image(src='images/lion.svg', width=240),
                                shader=ft.LinearGradient(
                                    colors=[ft.Colors.RED, ft.Colors.YELLOW, ft.Colors.ORANGE],
                                ),
                                blend_mode=ft.BlendMode.DST_OVER,
                            ),
                            gradient=ft.LinearGradient(
                                colors=[ft.Colors.RED, ft.Colors.YELLOW, ft.Colors.ORANGE],
                            ),
                            width=250,
                            height=250,
                            border_radius=150,
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=ft.ShaderMask(
                                content=ft.Image(src='images/shark.webp', width=200),
                                shader=ft.LinearGradient(
                                    colors=[ft.Colors.DEEP_PURPLE, ft.Colors.GREY, ft.Colors.BLUE],
                                ),
                                blend_mode=ft.BlendMode.SRC_IN,
                            ),
                            gradient=ft.RadialGradient(
                                colors=[ft.Colors.INDIGO, ft.Colors.BLUE_700],
                            ),
                            width=250,
                            height=250,
                            border_radius=150,
                            shadow=ft.BoxShadow(color=ft.Colors.WHITE, blur_radius=5),
                            alignment=ft.alignment.center,
                        ),
                        ft.ShaderMask(
                            content=ft.Image(src='images/dunk.svg', width=250),
                            shader=ft.RadialGradient(
                                colors=[ft.Colors.PURPLE, ft.Colors.AMBER],
                            ),
                            blend_mode=ft.BlendMode.SRC_IN,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True,
        ),
        expand=True,
        alignment=ft.alignment.center,
    )
    

    page.add(layout)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
