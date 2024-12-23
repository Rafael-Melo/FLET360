import flet as ft

def main(page: ft.Page):

    def show_bs(e):
        bs.open = True
        page.update()
    

    def close_bs(e):
        bs.open = False
        page.update()


    bs = ft.BottomSheet(
        content=ft.Container(
            ft.Column(
                controls=[
                    ft.Text(value='Título', style=ft.TextThemeStyle.HEADLINE_LARGE),
                    ft.Text(value='Conteúdo do bottomsheet', style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                    ft.FilledButton(text='Fechar', on_click=close_bs),
                ]
            ),
            padding=20,
        ),
        dismissible=False,
        enable_drag=True,
        is_scroll_controlled=False,
        maintain_bottom_view_insets_padding=True, # Margem inferior quando teclado virtual está ativo
        show_drag_handle=True, # Alça de arrasto
        elevation=2.0
    )

    page.overlay.append(bs)

    btn = ft.ElevatedButton(
        text='Abrir',
        on_click=show_bs,
    )

    page.add(btn)
    

if __name__ == '__main__':
    ft.app(target=main)
