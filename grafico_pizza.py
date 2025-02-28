import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLACK

    def on_chart_event(e: ft.PieChartEvent):
        for idx, section in enumerate(chart.sections):
            if idx == e.section_index:
                section.radius = 110
                section.title_style = ft.TextStyle(
                    size=16,
                    color=ft.Colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                    shadow=ft.BoxShadow(
                        blur_radius=2, color=ft.Colors.BLACK54,
                    )
                )
            else:
                section.radius=100
                section.title_style = ft.TextStyle(
                    size=12, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD,
                )
        
        chart.update()


    chart = ft.PieChart(
        expand=True,
        animate=ft.Animation(duration=1000, curve=ft.AnimationCurve.ELASTIC_IN_OUT),
        sections=[
            ft.PieChartSection(
                value=40,
                title='GELO',
                title_style=ft.TextStyle(
                    size=20,
                    color=ft.Colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                ),
                radius=200,
                title_position=0.5, # 0.0 - 1.0
                border_side=ft.BorderSide(width=5, color=ft.Colors.WHITE),
                badge=ft.Container(
                    content=ft.Icon(name=ft.Icons.AC_UNIT, color=ft.Colors.WHITE),
                    width=50,
                    height=50,
                    border=ft.border.all(width=2, color=ft.Colors.WHITE),
                    shape=ft.BoxShape.CIRCLE,
                    bgcolor=ft.Colors.BLACK,
                ),
                badge_position=0.98,
            ),
            ft.PieChartSection(
                value=20,
                color=ft.Colors.BROWN,
                title='TERRA',
                title_style=ft.TextStyle(
                    size=20,
                    color=ft.Colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                ),
                radius=200,
                title_position=0.5,
                border_side=ft.BorderSide(width=5, color=ft.Colors.WHITE),
                badge=ft.Container(
                    content=ft.Icon(name=ft.Icons.LOCAL_POLICE_OUTLINED, color=ft.Colors.WHITE),
                    width=50,
                    height=50,
                    border=ft.border.all(width=2, color=ft.Colors.WHITE),
                    shape=ft.BoxShape.CIRCLE,
                    bgcolor=ft.Colors.BLACK,
                ),
                badge_position=0.98,
            ),
            ft.PieChartSection(
                value=70,
                color=ft.Colors.RED_700,
                title='FOGO',
                title_style=ft.TextStyle(
                    size=20,
                    color=ft.Colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                ),
                radius=200,
                title_position=0.5,
                border_side=ft.BorderSide(width=5, color=ft.Colors.WHITE),
                badge=ft.Container(
                    content=ft.Icon(name=ft.Icons.LOCAL_FIRE_DEPARTMENT_SHARP, color=ft.Colors.WHITE),
                    width=50,
                    height=50,
                    border=ft.border.all(width=2, color=ft.Colors.WHITE),
                    shape=ft.BoxShape.CIRCLE,
                    bgcolor=ft.Colors.BLACK,
                ),
                badge_position=0.98,
            ),
            ft.PieChartSection(
                value=30,
                color=ft.Colors.DEEP_PURPLE,
                title='ÁGUA',
                title_style=ft.TextStyle(
                    size=20,
                    color=ft.Colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                ),
                radius=200,
                title_position=0.5,
                border_side=ft.BorderSide(width=5, color=ft.Colors.WHITE),
                badge=ft.Container(
                    content=ft.Icon(name=ft.Icons.WATER_DROP_OUTLINED, color=ft.Colors.WHITE),
                    width=50,
                    height=50,
                    border=ft.border.all(width=2, color=ft.Colors.WHITE),
                    shape=ft.BoxShape.CIRCLE,
                    bgcolor=ft.Colors.BLACK,
                ),
                badge_position=0.98,
            ),
            ft.PieChartSection(
                value=35,
                color=ft.Colors.YELLOW,
                title='RAIO',
                title_style=ft.TextStyle(
                    size=20,
                    color=ft.Colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                ),
                radius=200,
                title_position=0.5,
                border_side=ft.BorderSide(width=5, color=ft.Colors.WHITE),
                badge=ft.Container(
                    content=ft.Icon(name=ft.Icons.OFFLINE_BOLT, color=ft.Colors.WHITE),
                    width=50,
                    height=50,
                    border=ft.border.all(width=2, color=ft.Colors.WHITE),
                    shape=ft.BoxShape.CIRCLE,
                    bgcolor=ft.Colors.BLACK,
                ),
                badge_position=0.98,
            ),
            ft.PieChartSection(
                value=10,
                color=ft.Colors.GREEN_900,
                title='PLANTA',
                title_style=ft.TextStyle(
                    size=20,
                    color=ft.Colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                ),
                radius=200,
                title_position=0.5,
                border_side=ft.BorderSide(width=5, color=ft.Colors.WHITE),
                badge=ft.Container(
                    content=ft.Icon(name=ft.Icons.LOCAL_FLORIST_SHARP, color=ft.Colors.WHITE),
                    width=50,
                    height=50,
                    border=ft.border.all(width=2, color=ft.Colors.WHITE),
                    shape=ft.BoxShape.CIRCLE,
                    bgcolor=ft.Colors.BLACK,
                ),
                badge_position=0.98,
            ),
            ft.PieChartSection(
                value=15,
                color=ft.Colors.LIGHT_GREEN_100,
                title='VENTO',
                title_style=ft.TextStyle(
                    size=20,
                    color=ft.Colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                ),
                radius=200,
                title_position=0.5,
                border_side=ft.BorderSide(width=5, color=ft.Colors.WHITE),
                badge=ft.Container(
                    content=ft.Icon(name=ft.Icons.FLIGHT_SHARP, color=ft.Colors.WHITE),
                    width=50,
                    height=50,
                    border=ft.border.all(width=2, color=ft.Colors.WHITE),
                    shape=ft.BoxShape.CIRCLE,
                    bgcolor=ft.Colors.BLACK,
                ),
                badge_position=0.98,
            ),
        ],
        sections_space=10,
        center_space_radius=50,
        center_space_color=ft.Colors.GREY_900,
        start_degree_offset=90, # Rotação do início do gráfico
        on_chart_event=on_chart_event,
    )

    page.add(chart)


if __name__ == '__main__':
    ft.app(target=main)