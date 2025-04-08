import flet as ft
from flet.auth.providers import GitHubOAuthProvider
from dotenv import load_dotenv
import os
import pprint
from flet.security import encrypt, decrypt

load_dotenv()

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")

print("CLIENT_ID carregado:", GITHUB_CLIENT_ID is not None)
print("CLIENT_SECRET carregado:", GITHUB_CLIENT_SECRET is not None)

def main(page: ft.Page):
    page.title = "Login com GitHub"

    provider = GitHubOAuthProvider(
        client_id=GITHUB_CLIENT_ID,
        client_secret=GITHUB_CLIENT_SECRET,
        redirect_url='http://127.0.0.1:5354/oauth_callback'
    )

    def on_login(e: ft.LoginEvent):
        print("Login callback acionado!")
        if not e.error:
            pprint.pprint(page.auth.user)
            token = page.auth.token.to_json()
        else:
            print("Erro no login:", e.error)

    page.on_login = on_login

    page.add(
        ft.Column(
            [
                ft.Text("🚪 Faça login com o GitHub para continuar"),
                ft.ElevatedButton(
                    text="Login com GitHub",
                    on_click=lambda _: page.login(provider=provider)
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )


if __name__ == '__main__':
    ft.app(target=main)

# flet run .\aut_github.py -w --port 5354