import flet as ft
from flet.auth.providers import GoogleOAuthProvider
from dotenv import load_dotenv
import os
import pprint
from flet.security import encrypt, decrypt

load_dotenv()

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
SECRET = os.getenv("SECRET")

print("CLIENT_ID carregado:", GOOGLE_CLIENT_ID is not None)
print("CLIENT_SECRET carregado:", GOOGLE_CLIENT_SECRET is not None)

def main(page: ft.Page):
    page.title = "Login com GOOGLE"

    provider = GoogleOAuthProvider(
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        redirect_url='http://127.0.0.1:5354/oauth_callback',
    )

    encrypted_token = page.client_storage.get('google_token')
    if encrypted_token:
        try:
            saved_token = decrypt(encrypted_token, SECRET)
            page.login(provider=provider, saved_token=saved_token)
        except Exception as e:
            print("Erro ao usar token salvo. Redirecionando para login:", e)
            page.login(provider=provider)
    
    def show_login_screen():
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    ft.Text("🚪 Faça login com o GOOGLE para continuar"),
                    ft.ElevatedButton(
                        text="Login com GOOGLE",
                        on_click=lambda _: page.login(provider=provider)
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True
            )
        )
        page.update()

    def on_login(e: ft.LoginEvent):
        print("Login callback acionado!")
        if not e.error:
            pprint.pprint(page.auth.user)
            token = page.auth.token.to_json()
            encrypted_token = encrypt(token, SECRET)
            page.client_storage.set('google_token', encrypted_token)

            page.controls.clear()
            top_bar = ft.Row(
                controls=[
                    ft.CircleAvatar(
                        foreground_image_src=page.auth.user.get('picture'),
                        radius=20,
                    ),
                    ft.Text(
                        value=f"Olá, {page.auth.user.get('given_name')}!",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.IconButton(
                        icon=ft.Icons.LOGOUT,
                        tooltip="Sair",
                        on_click=lambda _: page.logout(),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )

            # Corpo principal
            body = ft.Column(
                controls=[
                    ft.Text("🎉 Bem-vindo ao seu dashboard!", size=30),
                    ft.Text("Aqui você poderá acessar todas as funcionalidades do sistema."),
                    # Adicione mais componentes aqui depois
                ],
                spacing=20,
            )

            # Adiciona tudo na página
            page.add(top_bar, ft.Divider(), body)
            page.update()
        else:
            print("Erro no login:", e.error)

    page.on_login = on_login

    def on_logout(e):
        print("Logout realizado.")
        page.client_storage.remove('google_token')
        page.controls.clear()
        page.update()

        # Recarrega a tela de login
        show_login_screen()
    
    page.on_logout = on_logout

    if page.auth and page.auth.user:
        page.add(
            ft.CircleAvatar(
                foreground_image_src=page.auth.user.get('picture')
            ),
            ft.Text(
                value=page.auth.user.get('given_name'),
                size=30,
            )
        )

        pprint.pprint(page.auth.user)
    
    else:
        show_login_screen()

if __name__ == '__main__':
    ft.app(target=main)

# flet run .\aut_google.py -w --port 5354
