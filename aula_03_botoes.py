import flet as ft

def main(page:ft.Page):
    #Botões
    page.scroll = True

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        bgcolor=ft.colors.GREEN,
        mini=True,
        shape=ft.CircleBorder(),
        tooltip='Cadastrar um novo produto',
        # text='Adicionar',
        on_click=lambda _: print('Fui clicado!'), # lambda pra função simples
    )

    page.update()

    container1 = ft.Container(
        content=ft.Row(
            controls=[
                ft.ElevatedButton(text='Clique aqui'),
                ft.ElevatedButton(text='Botão inativo', disabled=True),
                ft.ElevatedButton(text='Botão com ícone', icon=ft.icons.FAVORITE),
                ft.ElevatedButton(
                    text='Demais propriedades',
                    bgcolor=ft.colors.RED,
                    color=ft.colors.WHITE,
                    icon=ft.icons.FAVORITE_BORDER,
                    icon_color=ft.colors.AMBER,
                    tooltip='Olá, eu sou um botão',
                    url='https://google.com/'
                ),
            ]
            
        )
        
    )
    

    style = ft.ButtonStyle(
        color={
            ft.MaterialState.DEFAULT: ft.colors.BLACK,
            ft.MaterialState.HOVERED: ft.colors.WHITE,
        },
        bgcolor={
            '': ft.colors.AMBER,
            ft.MaterialState.DISABLED: ft.colors.GREEN,
            ft.MaterialState.FOCUSED: ft.colors.AMBER_200,
            'hovered': ft.colors.PINK,
        },
        padding={
            ft.MaterialState.DEFAULT: 10,
            ft.MaterialState.HOVERED: 20,
        },
        animation_duration=1000,
        side={
            ft.MaterialState.DEFAULT: ft.BorderSide(width=5, color=ft.colors.ORANGE_600),
            ft.MaterialState.HOVERED: ft.BorderSide(width=1, color=ft.colors.BLUE),
        },
        shape={
            ft.MaterialState.DEFAULT: ft.BeveledRectangleBorder(radius=10),
            ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=10),
        },
    )

    container2 = ft.Container(
        content=ft.Row(
            controls=[
                ft.ElevatedButton(
                    text='Botão com estilo personalizado',
                    style=style,
                    disabled=False
                ),
                ft.ElevatedButton(
                    text='Outro botão com estilo personalizado',
                    style=style,
                    disabled=False
                ),
            ]
        )
    )

    page.add(
        container1,
        container2,
    )

    def button_clicked(e):
        e.control.data += 1
        text.value = f'Botão acionado {e.control.data} vezes'
        # btn.data += 1
        # text.value = f'Botão acionado {btn.data} vezes'
        text.update()
        container3.update()

    container3 = ft.Container(
        content=ft.Row(
            controls=[
                ft.ElevatedButton(
                    text='Botão com contagem de clicks',
                    on_click=button_clicked,
                    data=0,
                ),
                ft.ElevatedButton(
                    text='Outro botão com contagem de clicks',
                    on_click=button_clicked,
                    data=10,
                )
            ]
        )
    )
    
    text = ft.Text()

    page.add(
        container3,
        text,
    )

    btn_style = ft.ButtonStyle(
        padding=50,
        animation_duration=1000,
        side={
            ft.MaterialState.DEFAULT: ft.BorderSide(10, color=ft.colors.BLUE),
            ft.MaterialState.HOVERED: ft.BorderSide(10, color=ft.colors.GREEN),
        },
        shape={
            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=0),
            ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=30),
        },
    )

    btnA = ft.FilledButton( # Cor do texto e bacgroudn seguem o tema do projeto, não pode ser alterado
        text='Botão primário',
        icon=ft.icons.STAR,
        icon_color=ft.colors.WHITE,
        style=btn_style,
        url='https://google.com/',
        tooltip='Click aqui para ir ao site',
    )

    trashbtn = ft.FilledButton(text='Trash', icon=ft.icons.DELETE, icon_color='red')
        
    page.add(
        btnA,
        trashbtn,
    )

    def on_image_click(e):
        print("Imagem clicada!")

    i_btn = ft.GestureDetector(
        content=ft.Container(
            content=ft.Image(
                src="icons/dragon.jpg",
                width=100,
                height=100,
                fit=ft.ImageFit.COVER,
            ),
            border_radius=ft.border_radius.all(50),
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            border=ft.border.all(5, "red"),
        ),
        on_tap=on_image_click,
        mouse_cursor=ft.MouseCursor.CLICK,
    )

    btnB = ft.FilledTonalButton(text='Botão Secundário')

    t_btn = ft.FilledTonalButton(text=" ", icon="info", icon_color="green")

    page.add(
        t_btn,
        i_btn,
        ft.Container(
            content=ft.Row(
                controls=[
                    btnB,
                    ft.FilledTonalButton(text='Botão Secundário Desabilitado', disabled=True, tooltip='Ação não permitida'),
                    ft.FilledTonalButton(text='Botão Secundário Com Ícone', icon=ft.icons.ADD),
                    ft.FilledTonalButton(text='Botão Secundário Com Ícone Colorido', icon=ft.icons.DANGEROUS, icon_color=ft.colors.CYAN_ACCENT_700),
                    ft.FilledTonalButton(text='Botão Secundário Com Estílo', style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),
                ]
            )
        )
    )

    page.add(
        ft.Container(
            content=ft.FloatingActionButton(text='Botão Flutuante'),
            bgcolor=ft.colors.GREY,
            height=250,
            alignment=ft.Alignment(x=0, y=0),
        )
    )

    def play_pause(e):
        e.control.selected = not e.control.selected
        e.control.tooltip = 'Pause' if e.control.selected else 'Play'
        e.control.update()


    container4 = ft.Container(
        content=ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.DELETE_FOREVER_ROUNDED,
                    icon_color=ft.colors.PINK,
                    icon_size=100,
                    tooltip='Deletar ação',
                ),
                ft.IconButton(
                    icon=ft.icons.PLAY_CIRCLE,
                    selected_icon=ft.icons.PAUSE_CIRCLE,
                    selected=False,
                    icon_size=100,
                    tooltip='Play',
                    on_click=play_pause,
                    style=ft.ButtonStyle(
                        color={
                            ft.MaterialState.SELECTED: ft.colors.WHITE,
                            ft.MaterialState.DEFAULT: ft.colors.RED,
                        }
                    )
                ),
                ft.IconButton(icon=ft.icons.DELETE_FOREVER_OUTLINED, icon_size=40, icon_color="red", tooltip="Apagar")
            ]
        )
    )

    page.add(
        container4,
    )

    o_btn = ft.OutlinedButton(
        text='Botão terciário',
        icon=ft.icons.ZOOM_IN,
        icon_color=ft.colors.TEAL,
        tooltip='Clique aqui',
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=5)
        ),
        url='https://google.com/',
        on_click=lambda _: print('Fui clicado 2!')
    )

    page.add(
        o_btn,
    )

    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        e.control.update()


    p_btn = ft.PopupMenuButton(
        icon=ft.icons.MENU_BOOK,
        items=[
            ft.PopupMenuItem(text='Item 1'),
            ft.PopupMenuItem(text='Item 2', icon=ft.icons.POWER_INPUT),
            ft.PopupMenuItem(
                content=ft.Row(
                    controls=[
                        ft.Icon(ft.icons.NOTIFICATION_IMPORTANT),
                        ft.Column(
                            controls=[
                                ft.Text(value='Rafael gostaria de enviar uma mensagem para você!', style=ft.TextThemeStyle.LABEL_LARGE, max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
                                ft.Text(value='Espero que você esteja gostando e aproveitando muito todo o curso de Flet!', style=ft.TextThemeStyle.LABEL_SMALL, max_lines=2, overflow=ft.TextOverflow.ELLIPSIS),
                            ],
                            width=200
                        ),
                    ],
                ),
                on_click=lambda _: print('Botão PopupMenu foi clicado!')
            ),
            ft.PopupMenuItem(),
            ft.PopupMenuItem(
                text='Selecione esse item',
                checked=False,
                on_click=check_item_clicked,
            ),
        ],
    )

    txt_btn = ft.TextButton(
        text='Editar',
        icon=ft.icons.EDIT,
        icon_color=ft.colors.WHITE,
        tooltip='Click para editar o texto',
        url='https://google.com/',
        style=ft.ButtonStyle(color=ft.colors.RED),
        on_click=lambda _: print('Editando conteúdo...')
    )

    txt2 = ft.TextButton(content=ft.Row([ft.Text("Ir para Página"), ft.Icon("arrow_forward")]), width=200)

    page.add(
        p_btn,
        txt_btn,
        txt2
    )


ft.app(target=main, assets_dir='assets')