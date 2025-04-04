import flet as ft

def main(page: ft.Page):
    page.padding = 0

    def list_tasks():
        page.bgcolor = ft.LinearGradient(colors=[ft.Colors.INDIGO_900, ft.Colors.DEEP_PURPLE])
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

    tx = ft.Text(value="ToDo", weight=ft.FontWeight.BOLD, size=30)
    tf = ft.TextField(hint_text='Digite uma tarefa', on_submit=save_localy)
    lv = ft.ListView()

    layout = ft.Container(
        content=ft.Column(
            controls=[tx, tf,lv,],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        expand=True,
            gradient=ft.LinearGradient(
                colors=[ft.Colors.INDIGO_900, ft.Colors.DEEP_PURPLE],
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
            ),
        alignment=ft.alignment.center,
    )

    page.add(layout)
    list_tasks()

    page.update()


if __name__ == '__main__':
    ft.app(target=main)
