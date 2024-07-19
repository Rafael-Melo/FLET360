import flet as ft

def main(page:ft.Page):
    #Textos
    icon1 = ft.Icon(name=ft.icons.FAVORITE, color=ft.colors.PINK)
    icon2 = ft.Icon(name=ft.icons.AUDIOTRACK, color=ft.colors.GREEN_400, size=50)
    icon3 = ft.Icon(name=ft.icons.BEACH_ACCESS, color=ft.colors.BLUE_400, size=80)
    icon4 = ft.Icon(name='settings', color='#C1C1C1', size=100, tooltip='Configurações')

    img = ft.Image(
        src='https://mir-s3-cdn-cf.behance.net/project_modules/max_3840/f5643096750899.5eb54f3381b8f.png',
        border_radius=ft.border_radius.all(20),
        height=600,
        width=600,
        fit=ft.ImageFit.CONTAIN, # Espaço que a imagem vai ocupar dentro do height e width
        repeat=ft.ImageRepeat.REPEAT
    )

    img2 = ft.Image(
        src='images/python.png',
        tooltip='Logo do Python', # Mensagem quando passa o mouse em cima
    )

    page.add(
        icon1,
        icon2,
        icon3,
        icon4,
        img,
        img2,
        )


ft.app(target=main, assets_dir='assets')