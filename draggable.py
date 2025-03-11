import flet as ft

def main(page: ft.Page):
    dg1 = ft.Row(
        controls=[
            ft.Draggable(
                group='color',
                content=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.Colors.CYAN,
                    border_radius=5,
                ),
                content_feedback=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.Colors.with_opacity(0.5, ft.Colors.PURPLE),
                    shape=ft.BoxShape.CIRCLE,
                ),
                content_when_dragging=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.Colors.GREY_100,
                )
            ),
            ft.Draggable(
                group='color',
                content=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.Colors.AMBER,
                    border_radius=5,
                ),
                content_feedback=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.Colors.with_opacity(0.5, ft.Colors.ORANGE),
                    shape=ft.BoxShape.CIRCLE,
                ),
                content_when_dragging=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.Colors.GREY_100,
                )
            ),
            ft.Draggable(
                group='color',
                content=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.Colors.RED,
                    border_radius=5,
                ),
                content_feedback=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.Colors.with_opacity(0.5, ft.Colors.PINK),
                    shape=ft.BoxShape.CIRCLE,
                ),
                content_when_dragging=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.Colors.GREY_100,
                )
            ),
            ft.Draggable(
                content=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.Colors.GREEN,
                    border_radius=5,
                ),
                content_feedback=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.Colors.with_opacity(0.5, ft.Colors.LIGHT_GREEN),
                    shape=ft.BoxShape.CIRCLE,
                ),
                content_when_dragging=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.Colors.GREY_100,
                )
            ),
        ]
    )

    def drag_will_accept(e):
        e.control.content.border = ft.border.all(
            5, ft.Colors.BLACK45 if e.data == 'true' else ft.Colors.RED
        )
        e.control.update()
    
    def drag_accept(e):
        src=page.get_control(e.src_id)
        e.control.content.bgcolor=src.content.bgcolor
        e.control.content.border=None
        e.control.update()
    
    def drag_leave(e):
        e.control.content.border=None
        e.control.update()

    target = ft.DragTarget(
        content=ft.Container(
            width=300,
            height=300,
            bgcolor=ft.Colors.GREY_100,
        ),
        group='color',
        on_will_accept=drag_will_accept,
        on_accept=drag_accept,
        on_leave=drag_leave,
    )

    page.add(dg1, target)


if __name__ == '__main__':
    ft.app(target=main)