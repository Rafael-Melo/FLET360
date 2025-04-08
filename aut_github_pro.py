import flet as ft
from flet.auth.providers import GitHubOAuthProvider
from dotenv import load_dotenv
import os
import pprint
from flet.security import encrypt, decrypt
import requests

load_dotenv()

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
SECRET = os.getenv("SECRET")

def main(page: ft.Page):
    page.title = "Login com GitHub"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = True

    provider = GitHubOAuthProvider(
        client_id=GITHUB_CLIENT_ID,
        client_secret=GITHUB_CLIENT_SECRET,
        redirect_url='http://127.0.0.1:5354/oauth_callback'
    )

    def render_logged_in():
        user_name = page.auth.user.get("name") or page.auth.user.get("login", "usuário")
        avatar_url = page.auth.user.get("avatar_url", "")

        headers = {"Authorization": f"{page.auth.token.token_type} {page.auth.token.access_token}"}
        repos_resp = requests.get('https://api.github.com/user/repos', headers=headers)
        user_repos = repos_resp.json()

        repo_cards = []

        for repo in user_repos:
            repo_url = repo["html_url"]

            repo_name = ft.Text(repo["name"], size=16, weight="bold", color=ft.colors.ON_SURFACE)
            repo_desc = ft.Text(repo["description"] or "Sem descrição", italic=True, color=ft.colors.ON_SURFACE)


            container = ft.Container(
                content=ft.Column(
                    [
                        repo_name,
                        repo_desc,
                        ft.Row(
                            [
                                ft.Icon(name=ft.icons.STAR_BORDER),
                                ft.Text(str(repo["stargazers_count"])),
                                ft.Icon(name=ft.icons.FOLDER),
                                ft.Text(repo["full_name"]),
                                ft.Icon(name=ft.icons.OPEN_IN_NEW, size=16, tooltip="Abrir repositório")
                            ],
                            spacing=10,
                        )
                    ],
                    spacing=5
                ),
                padding=10,
                bgcolor=ft.colors.SURFACE_VARIANT,
                border_radius=10,
                on_click=lambda e, url=repo_url: page.launch_url(url),
                ink=True
            )

            # hover simples — muda cor de fundo
            def on_hover(e, c=container):
                hover_on = e.data == "true"
                c.bgcolor = ft.colors.DEEP_PURPLE if hover_on else ft.colors.SURFACE_VARIANT
                repo_name.color = ft.colors.BLACK if hover_on else ft.colors.ON_SURFACE
                repo_desc.color = ft.colors.BLACK if hover_on else ft.colors.ON_SURFACE
                repo_name.update()
                repo_desc.update()
                c.update()

            container.on_hover = on_hover

            repo_cards.append(ft.Card(content=container, elevation=2))


        page.clean()
        page.add(
            ft.Column(
                [
                    ft.Text(f"👋 Bem-vindo, {user_name}!", size=24, weight="bold"),
                    ft.Image(src=avatar_url, width=100, height=100) if avatar_url else None,
                    ft.ElevatedButton(
                        text="Logout",
                        on_click=lambda _: page.logout()
                    ),
                    ft.Divider(height=30),
                    ft.Text("📦 Seus repositórios:", size=18, weight="w600"),
                    *repo_cards
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            )
        )
        pprint.pprint(page.auth.token)
        pprint.pprint(page.auth.user)

    def render_logged_out():
        page.clean()
        page.add(
            ft.Column(
                [
                    ft.Text("🚪 Faça login com o GitHub para continuar", size=30),
                    ft.ElevatedButton(
                        text="Login com GitHub",
                        on_click=lambda _: page.login(provider=provider)
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

    encrypted_token = page.client_storage.get('github_token')
    if encrypted_token:
        saved_token = decrypt(encrypted_token, SECRET)
        page.login(provider=provider, saved_token=saved_token)

    def on_login(e: ft.LoginEvent):
        print("🔐 Callback de login acionado")
        if e.error:
            print("❌ Erro ao logar:", e.error)
        else:
            print("✅ Login bem-sucedido!")
            render_logged_in()
            token = page.auth.token.to_json()
            encrypted_token = encrypt(token, SECRET)
            page.client_storage.set('github_token', encrypted_token)

    def on_logout(e):
        print("👋 Usuário deslogado")
        render_logged_out()

    page.on_login = on_login
    page.on_logout = on_logout

    if page.auth:
        render_logged_in()
    else:
        render_logged_out()

if __name__ == "__main__":
    ft.app(target=main)

# Para rodar:
# flet run ".\aut_github copy.py" -w --port 5354
