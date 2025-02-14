import flet as ft

def main(page:ft.Page):
    # Configurações da janela
    page.title = "Flet App"
    page.window_always_on_top = True
    page.window_title_bar_hidden = False
    page.window_full_screen = False
    # page.window_height = 300
    # page.window_max_height = 900
    # page.window_min_height = 200
    # page.window_width = 600
    # page.window_max_width = 900
    # page.window_min_width = 200
    # page.window_resizable = True
    # page.window_top = 100
    # page.window_left = 100
    page.window_movable = False # MAc e Linux
    page.window_prevent_close = True # MAc e Linux
    page.window_progress_bar = 0.5
    page.bgcolor = ft.colors.BLACK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_AROUND
    page.padding = 20
    page.spacing = 5
    page.fonts = {
        'Dragon Slayer': 'fonts/Dragon Slayer.ttf',
    }

    print(page.platform)

    def page_resized(e):
        print('Tamanho:', page.window_width, page.window_height)


    def window_event(e):
        match e.data:
            case 'moved':
                print('Moveu a página')
            case 'resized':
                print('Resize a página')
            case 'minimize':
                print('Minimizou a página')
            case _:
                print('Outra ação')


    page.on_window_event = window_event

    page.on_resize = page_resized

    mensagem=ft.Text(
        value='Olá Mundo! Bem vindo ao curso Flet 360!',
        style=ft.TextThemeStyle.DISPLAY_LARGE,
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        font_family='Dragon Slayer',
        italic=False,
        max_lines=2, # Máximo de linhas na quebra
        overflow=ft.TextOverflow.ELLIPSIS, # Simbolo quando corta o texto
        no_wrap=False, # Não quebrar linhas
        selectable=True,
        size=35,
        text_align=ft.TextAlign.CENTER,
        weight=ft.FontWeight.W_400
        )
    
    link_style = ft.TextStyle(color=ft.colors.BLUE, decoration=ft.TextDecoration.UNDERLINE)
    
    title_style = ft.TextStyle(
        color=ft.colors.RED,
        bgcolor=ft.colors.AMBER,
        decoration=ft.TextDecoration.OVERLINE,
        decoration_color=ft.colors.GREEN,
        decoration_thickness=5,
        decoration_style=ft.TextDecorationStyle.DASHED,
        italic=True,
        size=25,
        weight=ft.FontWeight.W_900
        )

    texto = ft.Text(
        spans=[
            ft.TextSpan(text='Texto com link ', style=link_style, url='http://www.google.com'),
            ft.TextSpan(text='continuação do texto... '),
            ft.TextSpan(text='Texto em destaque!!!', style=title_style),
        ],
        size=20
    )

    page.add(
        mensagem,
        texto
    )

    page.add(ft.Text(value='Meu nome é Rafael!'))

    elementos =[
        ft.Text(value='Elemento 1'),
        ft.Text(value='Elemento 2'),
        ft.Text(value='Elemento 3'),
        ft.Text(value='Elemento 4'),
        ft.Text(value='Elemento 5'),
    ]

    page.add(*elementos)

    texto01 = ft.Text(value='Texto 01')
    texto02 = ft.Text(value='Texto 02')
    texto03 = ft.Text(value='Texto 03')
    texto04 = ft.Text(value='Texto 04')
    texto05 = ft.Text(value='Texto 05')

    textos =ft.Row(
        controls=[
            texto01,
            texto02,
            texto03,
            texto04,
            texto05,
        ]
    )

    page.add(textos)


ft.app(target=main, assets_dir='assets')