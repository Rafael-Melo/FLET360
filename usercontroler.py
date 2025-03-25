import flet as ft
import time

class Product(ft.Container):
    def __init__(self, image: str, title: str, page: ft.Page):
        super().__init__()
        self.page = page # Armazena a referência da página
        self.title = title

        self.content = ft.Stack(
            controls=[
                ft.Image(
                    src=image,
                    fit=ft.ImageFit.COVER
                ),
                ft.Container(
                    content=ft.Text(
                        value=title,
                        size=30,
                        color=ft.Colors.BLACK,
                        weight=ft.FontWeight.BOLD
                    ),
                    alignment=ft.alignment.bottom_center,
                    padding=ft.padding.all(10),
                )
            ]
        )
        self.height=500,
        self.aspect_ratio=1.0
        self.alignment=ft.alignment.bottom_center
        self.padding=ft.padding.all(20)

    def did_mount(self):
        print(f'O produto \033[1;32m"{self.title}"\033[m foi inserido na página')
        return super().did_mount()
    
    def will_unmount(self):
        print(f'Removendo o produto \033[1;32m"{self.title}"\033[m da página')
        return super().will_unmount()
    
    def destroy(self):
        self.will_unmount()
        self.page.controls.remove(self)  # Remove o próprio objeto da página
        self.page.update()  # Atualiza a interface para refletir a remoção

def main(page: ft.Page):
    prod1 = Product(
        'https://deancadeiras.com.br/wp-content/uploads/2022/10/46395690fff65bdcc24035d489314fd9.png',
        'Cadeira Amarela de Escritório',
        page
    )

    prod2 = Product(
        'https://www.comfy.com.br/media/catalog/product/c/a/cadeira_gamer_xperience_ultra_vermelha_2.webp',
        'Cadeira Vermelha de Escritório',
        page
    )

    prod3 = Product(
        'https://m.media-amazon.com/images/I/519T9fP1cKL.jpg',
        'Cadeira Verde de Escritório',
        page
    )

    time.sleep(2)
    page.add(prod1)
    time.sleep(5)
    page.add(prod2)
    time.sleep(5)
    page.add(prod3)

    # time.sleep(2)
    # page.controls.clear()
    # page.update()

    # page.clean() ou prod1.clean() -- remove os componetes ou componente e atualiza a página mas não ativa o will_unmount()

    time.sleep(5)
    prod1.destroy()

if __name__ == '__main__':
    ft.app(target=main)
