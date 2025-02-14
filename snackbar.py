import flet as ft

def main(page: ft.Page):

    def show_sb(e):
        page.snack_bar.open = True
        page.update()
    

    page.snack_bar = ft.SnackBar(
        content=ft.Text(value='Não foi possível processar os dados nesse momento', weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
        bgcolor=ft.colors.GREY,
        show_close_icon=True,
        close_icon_color=ft.colors.RED,
        padding=ft.padding.all(50),
        duration=15000,
        behavior=ft.SnackBarBehavior.FLOATING,
        margin=ft.margin.all(20),
        dismiss_direction=ft.DismissDirection.HORIZONTAL, # Arrastar para fechar na direção
        action='Confirmar',
        action_color=ft.colors.GREEN,
        on_action=lambda _: print('Ação selecionada'),
    )

    btn = ft.ElevatedButton(text='Abrir Snackbar', on_click=show_sb)
    
    page.add(btn)


if __name__ == '__main__':
    ft.app(target=main)
