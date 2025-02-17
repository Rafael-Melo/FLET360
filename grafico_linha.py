import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = ft.padding.symmetric(horizontal=100)
    page.scroll = ft.ScrollMode.AUTO
    
    img = ft.Image(src='images/linha.png')
    page.add(img)

    chart = ft.LineChart(
        data_series=[
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(x=1, y=1,
                        point=ft.ChartCrossPoint(
                            color=ft.Colors.RED,
                            size=20,
                            width=10,
                        )
                    ),
                    ft.LineChartDataPoint(x=3, y=3,
                        show_tooltip=True,
                        tooltip='O valor é 2',
                        tooltip_align=ft.TextAlign.CENTER,
                        tooltip_style=ft.TextStyle(italic=True, color=ft.Colors.WHITE),
                        point=ft.ChartCirclePoint(
                            color=ft.Colors.AMBER,
                            radius=20,
                            stroke_width=5,
                        ),
                        selected_point=ft.ChartSquarePoint(
                            color=ft.Colors.GREEN,
                            size=20,
                            stroke_width=10,
                        ),
                        selected_below_line=ft.ChartPointLine(
                            color=ft.Colors.GREEN,
                            width=1,
                            dash_pattern=[50, 10] # Primeiro número tamanho da linha, segundo tamanho do espaço em branco
                        ),
                    ),
                    ft.LineChartDataPoint(x=5, y=1),
                    ft.LineChartDataPoint(x=6, y=2),
                    ft.LineChartDataPoint(x=7, y=5),
                    ft.LineChartDataPoint(x=8, y=3),
                ],
                curved=True,
                color=ft.Colors.AMBER_200,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.center_left,
                    end=ft.alignment.center_right,
                    colors=[ft.Colors.DEEP_ORANGE, ft.Colors.AMBER_200],
                ),
                stroke_width=10,
                stroke_cap_round=True,
                dash_pattern=[20, 10, 20, 15],
                above_line_bgcolor=ft.Colors.AMBER_100,
                above_line_gradient=ft.LinearGradient(
                    begin=ft.alignment.center_left,
                    end=ft.alignment.center_right,
                    colors=[ft.Colors.DEEP_ORANGE_100, ft.Colors.AMBER_100],
                ),
                below_line_bgcolor=ft.Colors.LIME_100,
                below_line_gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=[ft.colors.LIME, ft.Colors.with_opacity(0, ft.colors.LIME_100)],
                ),
                above_line_cutoff_y=3,
                below_line_cutoff_y=2,
                point=ft.ChartCrossPoint(
                    color=ft.Colors.AMBER,
                    size=20,
                    width=10,
                ),
                selected_point=ft.ChartCrossPoint(
                    color=ft.Colors.RED,
                    size=20,
                    width=10,
                ),
                above_line=ft.ChartPointLine(color=ft.Colors.BLACK, width=3),
                below_line=ft.ChartPointLine(color=ft.Colors.BLACK, width=3),
                selected_below_line=ft.ChartPointLine(color=ft.Colors.WHITE, width=3)
            )
        ],
        interactive=True,
        bgcolor=ft.Colors.GREY_200,
        tooltip_bgcolor=ft.Colors.BLACK,
        horizontal_grid_lines=ft.ChartGridLines(
            interval=1,
            color=ft.Colors.BLACK,
            width=1,
            dash_pattern=[10, 10],
        ),
        vertical_grid_lines=ft.ChartGridLines(
            interval=1,
            color=ft.Colors.BLACK,
            width=1,
            dash_pattern=[10, 10],
        ),
        left_axis=ft.ChartAxis(
            title=ft.Text(value='Eixo Y'),
            title_size=100, # Espaço do Texto
            show_labels=True,
            labels=[
                ft.ChartAxisLabel(value=1, label=ft.Text(value='R$ 1')),
                ft.ChartAxisLabel(value=2, label=ft.Text(value='R$ 2')),
                ft.ChartAxisLabel(value=3, label=ft.Text(value='R$ 3')),
                ft.ChartAxisLabel(value=4, label=ft.Text(value='R$ 4')),
                ft.ChartAxisLabel(value=5, label=ft.Text(value='R$ 5')),
            ],
            labels_interval=3,
            labels_size=50,
        ),
        bottom_axis=ft.ChartAxis(
            title=ft.Text(value='Eixo X'),
            title_size=50, # Espaço do Texto
            show_labels=True,
            labels=[
                ft.ChartAxisLabel(value=1, label=ft.Text(value='R$ JAN')),
                ft.ChartAxisLabel(value=2, label=ft.Text(value='R$ FEV')),
                ft.ChartAxisLabel(value=3, label=ft.Text(value='R$ MAR')),
                ft.ChartAxisLabel(value=4, label=ft.Text(value='R$ ABR')),
                ft.ChartAxisLabel(value=5, label=ft.Text(value='R$ MAI')),
                ft.ChartAxisLabel(value=5, label=ft.Text(value='R$ JUN')),
                ft.ChartAxisLabel(value=5, label=ft.Text(value='R$ JUL')),
                ft.ChartAxisLabel(value=5, label=ft.Text(value='R$ AGO')),
            ],
            labels_interval=1,
            labels_size=50,
        ),
        # right_axis=ft.ChartAxis(),
        # top_axis=ft.ChartAxis(),
        min_x=1,
        max_x=10,
        min_y=1,
        max_y=10,
    )

    page.add(chart)

    import random

    data=[
        ft.LineChartData(
            data_points=[ft.LineChartDataPoint(x=x, y=random.randint(0, 5)) for x in range(10)],
            curved=True,
        ),
        ft.LineChartData(
            data_points=[ft.LineChartDataPoint(x=x, y=random.randint(0, 5)) for x in range(10)],
            color=ft.Colors.GREEN,
        ),
        ft.LineChartData(
            data_points=[ft.LineChartDataPoint(x=x, y=random.randint(0, 5)) for x in range(10)],
            gradient=ft.LinearGradient(colors=[ft.Colors.PINK, ft.Colors.PURPLE]),
            stroke_width=5,
        ),
    ]

    page.add(
        ft.LineChart(data_series=data)
    )


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
