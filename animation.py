import flet as ft
import itertools

class AnimatedContainer(ft.Container):
    cores = itertools.cycle(['AMBER', 'PINK', 'CYAN'])
    def __init__(self, **kwargs):
        super().__init__()
        self.kwargs = kwargs
        self.content=None
        self.width=200
        self.height=200
        self.bgcolor=next(AnimatedContainer.cores)
        self.opacity=1
        self.offset=ft.transform.Offset(x=0, y=0)
        self.rotate=ft.transform.Rotate(angle=0, alignment=ft.alignment.center)
        self.scale=ft.transform.Scale(scale=1)
        self.animate=ft.animation.Animation(
            duration=1000,
            curve=ft.AnimationCurve.EASE_IN_OUT,
        )
        self.animate_opacity=True
        self.animate_offset=True
        self.animate_rotation=True
        self.animate_scale=True
        self.on_hover = kwargs.get("on_hover")
        self.on_click = kwargs.get("on_click")


def main(page: ft.Page):
    def animate_opacity(e):
        e.control.opacity = 0.1 if e.control.opacity == 1 else 1
        e.control.update()

    def animate_offset(e):
        e.control.offset = ft.transform.Offset(x = 0.5, y = 1) if e.control.offset.x == 0 else ft.transform.Offset(x = 0, y = 0)
        e.control.update()

    def animate_rotation(e):
        import math
        e.control.rotate.angle = math.radians(45) if e.control.rotate.angle == 0 else 0
        e.control.update()

    def animate_scale(e):
        e.control.scale.scale =0.5 if e.control.scale.scale == 1 else 1
        e.control.update()
    
    def animate_position(e):
        e.control.offset = (
            ft.transform.Offset(x=0, y=0) if e.control.offset.x == 0 else ft.transform.Offset(x=2, y=0)
        )
        e.control.update()


    page.add(
        ft.Column(
            controls=[
                AnimatedContainer(on_hover=animate_opacity),
                AnimatedContainer(on_hover=animate_offset),
                AnimatedContainer(on_hover=animate_rotation),
                AnimatedContainer(on_hover=animate_scale),
                AnimatedContainer(
                    offset=ft.transform.Offset(x=2, y=0),
                    animate_offset=True,
                    on_click=animate_position,
                ),
            ]
        )
    )


if __name__ == '__main__':
    ft.app(target=main)