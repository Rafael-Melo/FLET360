import flet as ft
import asyncio

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor=ft.Colors.BLACK

    img = ft.Image(
        src='images/dunk.svg',
        offset=ft.Offset(x=0, y=0),
        scale=1,
        opacity=0,
        animate_offset=ft.Animation(duration=3000, curve=ft.AnimationCurve.EASE),
        animate_scale=ft.Animation(duration=3000, curve=ft.AnimationCurve.EASE),
        animate_opacity=ft.Animation(duration=3000, curve=ft.AnimationCurve.EASE),
    )

    mask = ft.ShaderMask(
        content=img,
        shader=ft.RadialGradient(
            colors=[ft.Colors.PURPLE, ft.Colors.AMBER],
        ),
        expand=True,
        blend_mode=ft.BlendMode.SRC_IN,
    )
    
    layout = ft.Container(
        content=ft.Row(
            controls=[
                ft.Stack(
                    controls=[mask],
                    expand=True,
                ),
                ft.Text(value='RAFA MELO', size=45, weight=ft.FontWeight.BOLD, color=ft.Colors.DEEP_PURPLE)
            ]
        ),
        clip_behavior=ft.ClipBehavior.NONE,
    )
    

    async def animate(e = None):
        while True:
            img.offset.y = -0.3
            img.scale = 0.3
            img.opacity = 0
            img.update()
            await asyncio.sleep(3)

            img.offset.y = 0
            img.scale = 1
            img.opacity = 1
            img.update()
            await asyncio.sleep(3)

    page.add(layout)

    page.run_task(animate)

if __name__ == '__main__':
    ft.app(target=main)

# img = ft.Image(
#     src='https://gmedia.playstation.com/is/image/SIEPDC/dualsense-edge-listing-thumb-01-en-23aug22?$facebook$',
#     offset=ft.Offset(x=0, y=0),
#     scale=1,
#     opacity=1,
#     animate_offset=ft.Animation(duration=3000, curve=ft.AnimationCurve.EASE),
#     animate_scale=ft.Animation(duration=3000, curve=ft.AnimationCurve.EASE),
#     animate_opacity=ft.Animation(duration=3000, curve=ft.AnimationCurve.EASE),
# )