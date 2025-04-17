import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.WHITE

    def move_backward(e):
        carousel.scroll_to(delta=-100, duration=300, curve=ft.AnimationCurve.DECELERATE)
        carousel.update()
    
    def move_forward(e):
        carousel.scroll_to(delta=100, duration=300, curve=ft.AnimationCurve.DECELERATE)
        carousel.update()

    titulo = ft.Text(value='Carrocel', size=50, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_ACCENT)
        
    layout = ft.Container(
        shadow=ft.BoxShadow(blur_radius=100),
        content=ft.Column(
            controls=[
                carousel := ft.Row(
                    scroll=ft.ScrollMode.HIDDEN,
                    controls=[
                        ft.Image(
                            src=f'https://picsum.photos/250/300?{num}'
                        ) for num in range(10)
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        ft.IconButton(icon=ft.Icons.KEYBOARD_ARROW_LEFT, on_click=move_backward),
                        ft.IconButton(icon=ft.Icons.KEYBOARD_ARROW_RIGHT, on_click=move_forward),
                    ]
                )
            ],
        )
    )

    page.add(titulo, layout)


if __name__ == '__main__':
    ft.app(target = main)
