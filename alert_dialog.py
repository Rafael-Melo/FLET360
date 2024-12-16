import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER

    def close_ad(e):
        ad1.open = False
        page.update()

    
    ad1 = ft.AlertDialog(
        title=ft.Text(value='Aviso Importante'),
        content=ft.Text(value='Você está prestes a deletar os dados da sessão. Quer mesmo seguir?'),
        content_padding=ft.padding.all(30),
        inset_padding=ft.padding.all(10),
        modal=True,
        shape=ft.RoundedRectangleBorder(radius=5),
        on_dismiss=lambda _: print('Fechei'),

        actions=[
            ft.TextButton(text='Cancelar', style=ft.ButtonStyle(color=ft.colors.RED), on_click=close_ad),
            ft.ElevatedButton(text='Salvar', style=ft.ButtonStyle(bgcolor=ft.colors.GREEN, color=ft.colors.WHITE), on_click=close_ad),
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )

    def open_ad(e):
        page.dialog = ad1
        ad1.open = True
        page.update()

    
    btn1 = ft.ElevatedButton(text='Abrir Popup', on_click=open_ad)

    page.add(btn1)


if __name__ == '__main__':
    ft.app(target=main)
