import flet as ft

def main(page: ft.Page):
    page.padding = ft.padding.symmetric(vertical=100, horizontal=20)

    tf = ft.TextField(
        label='E-Mail',
        label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
        
        text_align=ft.TextAlign.RIGHT,
        text_size=20,
        text_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
        
        # value='Conteúdo pré preenchido',
        
        bgcolor=ft.colors.BLACK45,
        border=ft.InputBorder.OUTLINE,
        border_color=ft.colors.WHITE,
        border_radius=ft.border_radius.all(50),
        border_width=2,
        color=ft.colors.AMBER,
        content_padding=ft.padding.all(20),

        capitalization=ft.TextCapitalization.WORDS,

        counter_text='Texto',
        counter_style=ft.TextStyle(size=40, italic=True),

        cursor_color=ft.colors.DEEP_ORANGE,
        cursor_height=20,
        cursor_radius=10,
        cursor_width=5,
        dense=True, # Ajusta o tamanho quando há muitos textfilds na tela

        # error_text='Valor inválido',
        # error_style=ft.TextStyle(size=20),
        helper_text='Seu melhor e-mail',
        helper_style=ft.TextStyle(italic=True),
        hint_text='eu@email.com',
        hint_style=ft.TextStyle(italic=True),

        # filled=True, # Cor de fundo de acordo com o tema
        focused_bgcolor=ft.colors.LIGHT_GREEN,
        focused_border_color=ft.colors.GREEN,
        focused_border_width=5,
        focused_color=ft.colors.WHITE,

        icon=ft.icons.EMAIL,
        # input_filter=ft.InputFilter(
        #     allow=False,
        #     regex_string=r"[0-9]",
        #     replacement_string='-',
        # ),
        # input_filter=ft.NumbersOnlyInputFilter(),
        # input_filter=ft.TextOnlyInputFilter(),

        # keyboard_type=ft.KeyboardType.NUMBER,
        # max_length=5,
        # max_lines=3,
        # min_lines=2,
        # multiline=True, # Permite apertar enter para ir para linha de baixo
        # password=True,
        # can_reveal_password=True,

        prefix_text='https://',
        prefix_icon=ft.icons.LINK,
        prefix_style=ft.TextStyle(size=20),
        suffix_text='.com.br',

        # read_only=True,

        on_change=lambda x: print(x.data),
    )

    page.add(tf)


if __name__ == '__main__':
    ft.app(target = main, view = ft.AppView.FLET_APP)