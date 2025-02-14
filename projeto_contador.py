import flet as ft

def main(page: ft.Page):
    page.title = 'Contador'
    page.window.height =200
    page.window.width = 300
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    text_number = ft.TextField(value='0', text_align=ft.TextAlign.CENTER, width=100)

    def minus_click(e):
        text_number.value = int(text_number.value) - 1
        text_number.update()
    

    def plus_click(e):
        text_number.value = int(text_number.value) + 1
        text_number.update()
    

    page.add(
        ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.REMOVE, on_click=minus_click),
                text_number,
                ft.IconButton(icon=ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


if __name__ == '__main__':
    ft.app(target=main)
