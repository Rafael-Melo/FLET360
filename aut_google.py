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
        redirect_url='http://127.0.0.1:5354/oauth_callback'
    )

    encrypted_token = page.client_storage.get('google_token')
    if encrypted_token:
        saved_token = decrypt(encrypted_token, SECRET)
        page.login(provider=provider, saved_token=saved_token)

    def on_login(e: ft.LoginEvent):
        print("Login callback acionado!")
        if not e.error:
            pprint.pprint(page.auth.user)
            token = page.auth.token.to_json()
            encrypted_token = encrypt(token, SECRET)
            page.client_storage.set('google_token', encrypted_token)
        else:
            print("Erro no login:", e.error)

    page.on_login = on_login

    page.add(
        ft.Column(
            [
                ft.Text("🚪 Faça login com o GOOGLE para continuar"),
                ft.ElevatedButton(
                    text="Login com GOOGLE",
                    on_click=lambda _: page.login(provider=provider)
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )


if __name__ == '__main__':
    ft.app(target=main)

# flet run .\aut_google.py -w --port 5354