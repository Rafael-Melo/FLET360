import flet as ft

# Markdown precisa estar colado no começo da linha
mk_text ="""
# Esse é o título
### esse é o subtítulo
- Item 1
- Item 2

1. Item 1
2. Item 2

**Texto em negrito**
_Texto em itálico_
"""


def main(page: ft.Page):
    page.scroll =  ft.ScrollMode.AUTO

    with open('./markdown.md') as f:
        markdown = f.read()

    md1 = ft.Markdown(
        value=markdown,
        selectable=True,
        extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
        on_tap_link=lambda e: page.launch_url(e.data),
        code_theme='monokai-sublime'
    )

    md2 = ft.Markdown(
        value=mk_text
    )

    page.add(md2)


if __name__ == '__main__':
    ft.app(target=main)
