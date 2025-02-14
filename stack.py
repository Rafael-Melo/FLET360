import flet as ft

def main(page: ft.Page):
    st = ft.Stack(
        controls=[
            ft.Container(
                image_src='https://w0.peakpx.com/wallpaper/450/411/HD-wallpaper-monkey-king-monkey-king-sun-wukong.jpg',
                image_fit=ft.ImageFit.COVER,
            ),
            ft.Container(
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_left,
                    colors=[ft.Colors.RED, ft.Colors.YELLOW_900],
                ),
                opacity=0.3,
            ),
            ft.Text(value='WUKONG', style=ft.TextThemeStyle.TITLE_LARGE, color=ft.Colors.WHITE, size=40, left=30,),
            ft.Column(
                top=100,
                left=50,
                right=0,
                bottom=0,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(value='ATK: 08', style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                            ft.Icon(ft.icons.STAR, size=30),
                        ],
                    ),
                    ft.Row(
                        controls=[
                            ft.Text(value='DEF: 05', style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                            ft.Icon(ft.icons.SHIELD_SHARP, size=30),
                        ],
                    ),
                    ft.Row(
                        controls=[
                            ft.Text(value='SPD: 10', style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                            ft.Icon(ft.icons.SPEED, size=30),
                        ],
                    ),
                ]
            ),
        ],
        # expand=True,
        aspect_ratio=1.77,
    )

    page.add(st)


if __name__ == '__main__':
    ft.app(target=main)
