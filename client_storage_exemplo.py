import flet as ft

def main(page: ft.Page):
    page.client_storage.set('Chave', 'valor')
    dado_salvo = page.client_storage.get('Chave')

    page.add(ft.Text(value=dado_salvo))

    dado_inexistente = page.client_storage.get('chave2')
    print(dado_inexistente)

    page.client_storage.set('produto_1', 'Cadeira')
    page.client_storage.set('produto_2', 'Sofá')
    page.client_storage.set('produto_3', 'Armário')
    page.client_storage.set('produto_4', 'Mesa')
    page.client_storage.set('produto_5', 'Estante')
    todos_as_chaves = page.client_storage.get_keys('produto_')

    # page.client_storage.remove('produto_1')

    lista = []
    for chave in todos_as_chaves:
        valor = page.client_storage.get(chave)
        lista.append(valor)
        
    page.add(ft.ListView(controls=[ft.Text(p) for p in lista]))

    page.client_storage.set('todo.tarefas', ['Tarefa_1', 'Tarefa_2', 'Tarefa_3'])
    lista_tarefas = page.client_storage.get('todo.tarefas')
    print(lista_tarefas, type(lista_tarefas))

    page.client_storage.set('ecommerce.catalogo.produto_1', 'Cadeira Gamer')
    page.client_storage.set('ecommerce.carrinho.produto_1', 'Echo Dot')
    page.client_storage.set('ecommerce.pedidos.produto_1', 'Fone de Ouvido')

    # page.client_storage.clear()


if __name__ == '__main__':
    ft.app(target=main)
