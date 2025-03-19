import flet as ft

def main(page: ft.Page):
    def on_keyboard(e: ft.KeyboardEvent):
        print(e)

        tecla = ''

        if e.ctrl:
            tecla += 'Ctrl + '

        if e.shift:
            tecla += 'Shift + '

        if e.alt:
            if page.platform == 'macos':
                tecla += 'Opt + '
            else:
                tecla += 'Alt + '
        
        if e.meta:
            if page.platform == 'macos':
                tecla += 'Cmd + '
            else:
                tecla += 'Win + '

        tecla += e.key
        page.add(ft.Text(value=tecla))

        if e.shift and e.key == 'A':
            page.add(ft.Text(value='Você selecionou o atalho Shift + A'))
        
        if e.ctrl and e.key == 'C':
            page.add(ft.Text(value='Copiando os dados para área de transferência'))
        
    
    page.on_keyboard_event = on_keyboard
    page.add(
        ft.Text('Aperte algum botão')
    )


if __name__ == '__main__':
    ft.app(target=main)