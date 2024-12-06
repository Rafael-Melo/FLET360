import flet as ft

def main(page: ft.Page):
    page.padding = 0
    page.title = "Markdown Editor"

    def update_view(e):
        view.value = editor.value
        view.update()


    editor = ft.TextField(
        multiline=True,
        min_lines=30,
        max_lines=30,
        color=ft.colors.BLACK,
        content_padding=ft.padding.all(30),
        border=ft.InputBorder.NONE,
        bgcolor=ft.colors.BLUE_GREY,
        on_change=update_view
    )

    how_to = ft.Container(
        expand=True,
        padding=ft.padding.all(30),
        content=ft.Column(
            scroll=ft.ScrollMode.ALWAYS,
            controls=[
                ft.Text(value='Para criar títulos de diferentes tamanhos', weight=ft.FontWeight.BOLD, color=ft.colors.BLACK, selectable=True),
                ft.Text(value='# H1', color=ft.colors.GREY_700, selectable=True),
                ft.Text(value='## H2', color=ft.colors.GREY_700, selectable=True),
                ft.Text(value='### H3', color=ft.colors.GREY_700, selectable=True),
                ft.Divider(color=ft.colors.GREY, height=40),

                ft.Text(value='Para formatar o texto', weight=ft.FontWeight.BOLD, color=ft.colors.BLACK, selectable=True),
                ft.Text(value='**Texto em negrito**', color=ft.colors.GREY_700, selectable=True),
                ft.Text(value='*Texto em itálico*', color=ft.colors.GREY_700, selectable=True),
                ft.Text(value='~~Texto tachado~~', color=ft.colors.GREY_700, selectable=True),
                ft.Divider(color=ft.colors.GREY, height=40),

                ft.Text(value='Para criar listas', weight=ft.FontWeight.BOLD, color=ft.colors.BLACK, selectable=True),
                ft.Text(value='1. Ordenada', color=ft.colors.GREY_700, selectable=True),
                ft.Text(value='- Não ordenada', color=ft.colors.GREY_700, selectable=True),
                ft.Divider(color=ft.colors.GREY, height=40),

                ft.Text(value='Para inserir links e imagens', weight=ft.FontWeight.BOLD, color=ft.colors.BLACK, selectable=True),
                ft.Text(value='[Texto do link](https://google.com)', color=ft.colors.GREY_700, selectable=True),
                ft.Text(value='![Label da imagem](images/python.png)', color=ft.colors.GREY_700, selectable=True),
                ft.Divider(color=ft.colors.GREY, height=40),

                ft.Text(value='Para inserir código', weight=ft.FontWeight.BOLD, color=ft.colors.BLACK, selectable=True),
                ft.Text(value='`print("Código em uma linha")`', color=ft.colors.GREY_700, selectable=True),
                ft.Text(value='```\nprint("Código em múltiplas linhas")\n```', color=ft.colors.GREY_700, selectable=True),
                ft.Divider(color=ft.colors.GREY, height=40),
            ]
        )
    )

    view = ft.Markdown(
        value=editor.value,
        selectable=True,
        extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
        code_theme='monokai-sublime',
        on_tap_link=lambda e: page.launch_url(e.data),
    )

    layout = ft.Row(
        expand=True,
        spacing=0,
        vertical_alignment=ft.CrossAxisAlignment.STRETCH,
        controls=[
            ft.Container(
                expand=True,
                bgcolor=ft.colors.WHITE,
                content=ft.Column(
                    controls=[
                        editor,
                        how_to
                    ]
                )
            ),
            ft.Container(
                expand=True,
                bgcolor=ft.colors.BLACK,
                padding=ft.padding.all(30),
                content=view,
            ),
        ]
    )

    page.add(layout)


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')

"""# **Para criar títulos de diferentes tamanhos**
# H1
## H2
### H3
----------------------------------------------------

# **Para formatar o texto**
**Texto em negrito**

*Texto em itálico*

~~Texto tachado~~

----------------------------------------------------

# **Para criar listas**
1. Ordenada
- Não ordenada
----------------------------------------------------

# **Para inserir links e imagens**
**[Site Oficial](https://google.com)**
![Label da imagem](images/python.png)

----------------------------------------------------

# **Para inserir código'**
`print("Código em uma linha")`
```python
import flet as ft

def main(page: ft.Page):
    coluna = ft.Column(
        controls=[
            ft.Text('Python'),
            ft.Text('Flet'),
    )

    page.add(coluna)

if __name__ == "__main__":
    ft.app(target=main)
```
----------------------------------------------------"""