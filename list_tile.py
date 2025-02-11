import flet as ft

def main(page: ft.Page):
    lt1 = ft.ListTile(
        title=ft.Text(value='Título do primeiro'),
        subtitle=ft.Text(value='Subtítulo do primeiro'),
        leading=ft.Icon(name=ft.Icons.ADB),
        trailing=ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(text='Item 01'),
                ft.PopupMenuItem(text='Item 02'),
            ]
        ),
        content_padding=ft.padding.all(20),
        selected=True,
        on_click=lambda _: print('Primeiro clicado'),
        url='https://www.google.com/',
    )

    lt2 = ft.ListTile(
        title=ft.Text(value='Título do segundo'),
        subtitle=ft.Text(value='Subtítulo do segundo...'),
        leading=ft.Icon(name=ft.Icons.ADB),
        trailing=ft.Text(value='3', size=20),
        content_padding=ft.padding.all(20),
        selected=True,
        on_click=lambda _: print('Segundo clicado'),
    )

    lt3 = ft.ListTile(
        title=ft.Text(value='Título do terceiro'),
        leading=ft.Icon(name=ft.Icons.ADB),
        trailing=ft.Switch(),
        toggle_inputs=True,
        on_click=lambda _: print('Terceiro clicado'),
    )

    page.add(lt1, lt2, lt3)


if __name__ == '__main__':
    ft.app(target=main)