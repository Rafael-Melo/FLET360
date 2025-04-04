import flet as ft

def main(page: ft.Page):
    def list_tasks():
        items = page.client_storage.get('tasks')

        if not items:
            items = []

        def change_state(e):
            item = {'label': e.control.label, 'selected': e.control.value}
            items[e.control.data] = item
            page.client_storage.set('tasks', items)
        
        lv.controls=[
            ft.Checkbox(
                value=item.get('selected'),
                label=item.get('label'),
                adaptive=True,
                data=index,
                on_change=change_state
            ) for index, item in enumerate(items)
        ]

        lv.update()

    def save_localy(e):
        item = {'label': e.control.value, 'selected': False}
        items = page.client_storage.get('tasks')

        if not items:
            items = []

        items.append(item)

        page.client_storage.set('tasks', items)
        e.control.value = ''
        e.control.update()
        list_tasks()

    tf = ft.TextField(on_submit=save_localy)
    lv = ft.ListView()

    page.add(tf, lv)
    list_tasks()


if __name__ == '__main__':
    ft.app(target=main)
