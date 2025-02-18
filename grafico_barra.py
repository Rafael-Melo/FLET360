import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = ft.padding.symmetric(horizontal=100)
    page.scroll = ft.ScrollMode.AUTO

    img = ft.Image(src='images/barra.png')
    page.add(img)

    chart = ft.BarChart(
        expand=True,
        bar_groups=[
            ft.BarChartGroup(
                x=0,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=40,
                        to_y=80,
                        width=40,
                        color=ft.Colors.PINK,
                        tooltip='Fuji',
                        border_radius=0,
                        show_tooltip=True,
                    ),
                    ft.BarChartRod(
                        from_y=0,
                        to_y=40,
                        width=40,
                        color=ft.Colors.LIGHT_GREEN,
                        tooltip='Verde',
                        border_radius=0,
                        border_side=ft.BorderSide(width=2, color=ft.Colors.GREEN),
                    ),
                ],
                bars_space=20,
                group_vertically=True, # Empilha as barra
            ),
            ft.BarChartGroup(
                x=1,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=100,
                        width=40,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.bottom_center,
                            end=ft.alignment.top_center,
                            colors=[ft.Colors.DEEP_PURPLE, ft.Colors.PURPLE],
                        ),
                        border_radius=ft.border_radius.vertical(top=20),
                        tooltip='Jabuticaba',
                    ),
                ]
            ),
            ft.BarChartGroup(
                x=2,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=30,
                        width=40,
                        color=ft.Colors.RED,
                        tooltip='Morango',
                        border_radius=0,
                        bg_color=ft.Colors.GREY_300,
                        bg_from_y=0,
                        bg_to_y=100,
                        bg_gradient=ft.LinearGradient(
                            colors=[ft.Colors.DEEP_ORANGE, ft.Colors.YELLOW],
                        )
                    )
                ]
            ),
            ft.BarChartGroup(
                x=2,
                bar_rods=[
                    ft.BarChartRod(
                        rod_stack_items=[
                            ft.BarChartRodStackItem(
                                from_y=10,
                                to_y=30,
                                color=ft.Colors.YELLOW,
                            ),
                            ft.BarChartRodStackItem(
                                from_y=0,
                                to_y=10,
                                color=ft.Colors.RED,
                                border_side=ft.BorderSide(width=5, color=ft.Colors.RED_ACCENT)
                            ),
                        ],
                        from_y=0,
                        to_y=60,
                        width=40,
                        color=ft.Colors.ORANGE,
                        border_radius=0,
                        tooltip='Laranja'
                    )
                ]
            )
        ],
        border=ft.border.all(width=5, color=ft.Colors.GREY_400),
        interactive=True,
        tooltip_bgcolor=ft.Colors.BLACK,
    )

    page.add(chart)


if __name__ == '__main__':
    ft.app(target=main)