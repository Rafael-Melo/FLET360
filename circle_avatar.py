import flet as ft

def main(page: ft.Page):
    av1 = ft.CircleAvatar(
        foreground_image_url='https://img.freepik.com/vetores-premium/orgulhoso-viking-avatar-estilizado-plano-desenhando-graficos-avatar-mitos-lendas-meia-idade-barba-jogos-fantasia-destemido-guerreiro-conceito-criativo-ilustracao-vetorial-generative-ai_748571-1019.jpg',
        radius=200,
        tooltip='Programador Viking',
    )

    av2 = ft.CircleAvatar(
        bgcolor=ft.colors.AMBER,
        color=ft.colors.WHITE,
        content=ft.Text(
            value='PV'
        ),
        max_radius=200,
        min_radius=100,
        tooltip='Usuário PV',
    )

    av3 = ft.Badge(
        content=av1,
        bgcolor=ft.colors.GREEN,
        small_size=100,
    )


    page.add(av1, av2, av3)

if __name__ == '__main__':
    ft.app(target=main)
