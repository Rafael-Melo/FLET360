import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = ft.padding.symmetric(horizontal=100)
    page.scroll = ft.ScrollMode.AUTO

    img = ft.Image(src='images/barra.png')
    page.add(img)

    def chart_events(e: ft.BarChartEvent):
        if e.group_index is not None:
            chart.bar_groups[e.group_index].bars_space = 20
            chart.bar_groups[e.group_index].bar_rods[e.rod_index].color = ft.Colors.GREY
            chart.update()


    chart = ft.BarChart(
        expand=True,
        animate=ft.Animation(duration=1000, curve=ft.AnimationCurve.ELASTIC_IN_OUT),
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
                group_vertically=False, # Empilha as barra
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
        horizontal_grid_lines=ft.ChartGridLines(
            interval=20,
            color=ft.Colors.GREEN_300,
            width=3,
            dash_pattern=[3, 20]
        ),
        vertical_grid_lines=ft.ChartGridLines(
            interval=0.1,
            color=ft.Colors.GREY_300,
            width=1,
        ),
        left_axis=ft.ChartAxis(
            labels_size=40,
            show_labels=True,
            labels_interval=30,
            title=ft.Text(value='Preço das Frutas (R$)'),
            title_size=100,
        ),
        top_axis=ft.ChartAxis(
            show_labels=False,
            title=ft.Text(value='Preço Médio das Frutas em São Paulo', size=30),
            title_size=100,
        ),
        right_axis=ft.ChartAxis(
            show_labels=False,
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=0,
                    label=ft.Container(ft.Text('Maçã'), padding=10),
                ),
                ft.ChartAxisLabel(
                    value=1,
                    label=ft.Container(ft.Text('Jabuticaba'), padding=10),
                ),
                ft.ChartAxisLabel(
                    value=2,
                    label=ft.Container(ft.Text('Morango'), padding=10),
                ),
                ft.ChartAxisLabel(
                    value=3,
                    label=ft.Container(ft.Text('Laranja'), padding=10),
                ),
            ],
            labels_size=40,
        ),
        min_y=0,
        max_y=120,
        on_chart_event=chart_events,
    )

    page.add(chart)


if __name__ == '__main__':
    ft.app(target=main)