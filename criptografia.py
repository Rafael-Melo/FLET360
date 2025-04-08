import flet as ft
import os
from flet.security import encrypt, decrypt

def main(page: ft.Page):
    # secret_key = os.getenv("SECRET_KEY")
    secret_key = 'A1FD1DWSA2FAS12FASDA1G13K'

    texto = 'Dado privado que não deve ser exposto'

    # Criptogrfar
    
    texto_criptografado = encrypt(texto, secret_key)
    
    page.add(ft.Text(value=texto_criptografado))

    # Decriptografar
    texto_descriptografado = decrypt(texto_criptografado, secret_key)

    page.add(ft.Text(value=texto_descriptografado))

    page.client_storage.set('senha', texto)
    page.client_storage.set('senha', texto_criptografado)

    import secrets
    chave = secrets.token_hex(30)
    page.add(ft.Text(value=chave, size=20))


if __name__ == '__main__':
    ft.app(target=main)

# pip install cryptography