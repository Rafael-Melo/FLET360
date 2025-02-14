import flet as ft

def main(page: ft.Page):
    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(
                text='Tab 1',
                content=ft.Container(
                    padding=ft.padding.all(30),
                    content=ft.Text('Conteúdo da TAB 1'),
                )
            ),
            ft.Tab(
                text='Tab 2',
                content=ft.Container(
                    padding=ft.padding.all(30),
                    content=ft.Text('Não é o conteúdo da TAB 1'),
                )
            ),
            ft.Tab(
                tab_content=ft.Container(
                    content=ft.Stack(
                        controls=[
                            ft.CircleAvatar(
                                foreground_image_url="https://avatars.githubusercontent.com/u/144709944?s=200&v=4",
                                radius=20,
                            ),
                            ft.Container(
                                content=ft.Text("1", size=10, color="white"),
                                bgcolor=ft.colors.RED,
                                width=15,
                                height=15,
                                border_radius=7,
                                alignment=ft.alignment.center,
                                right=0,
                                top=0,
                            ),
                        ],
                    ),
                ),
                content=ft.Container(
                    padding=ft.padding.all(30),
                    content=ft.Text("Perfil do Usuário"),
                ),
            ),
            # ft.Tab(
            #     tab_content=ft.Container(
            #         content=ft.Badge(
            #             bgcolor=ft.colors.GREEN,
            #             content=ft.CircleAvatar(
            #                 foreground_image_url='https://avatars.githubusercontent.com/u/144709944?s=200&v=4',
            #                 tooltip='DEV',
            #             ),
            #             small_size=10,
            #         )
            #     ),
            #     content=ft.Container(
            #         padding=ft.padding.all(30),
            #         content=ft.Text("Perfil do Usuário"),
            #     ),
            # ),
            ft.Tab(
                icon=ft.icons.SETTINGS,
                content=ft.Container(
                    padding=ft.padding.all(30),
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.ElevatedButton(text="Bt 01"),
                            ft.ElevatedButton(text="Bt 02"),
                            ft.ElevatedButton(text="Bt 03"),
                        ],
                    ),
                ),
            ),
        ],
        expand=1,
        animation_duration=1000,
        divider_color=ft.colors.BLUE,
        indicator_border_radius=ft.border_radius.all(10),
        indicator_color=ft.colors.WHITE,
        indicator_padding=ft.padding.all(5),
        indicator_tab_size=False,
        label_color=ft.colors.GREEN,
        unselected_label_color=ft.colors.GREY,
        overlay_color={
            ft.MaterialState.HOVERED: ft.colors.WHITE24,
        },
        scrollable=False,
    )

    page.add(tabs)


if __name__ == '__main__':
    ft.app(target=main)
