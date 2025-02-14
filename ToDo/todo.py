import flet as ft
import sqlite3

class ToDo:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.Colors.BLACK
        self.page.window_width = 350
        self.page.window_height = 450
        self.page.window_resizable = False
        self.page.window.always_on_top = True
        self.page.scroll = ft.ScrollMode.ALWAYS
        self.page.title = 'ToDo App'
        self.task = ''
        self.view = 'all'
        self.db_execute('CREATE TABLE IF NOT EXISTS tasks(name, status)')
        self.results = self.db_execute('SELECT * FROM tasks')
        self.main_page()

    
    def db_execute(self, query, params=[]):
        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute(query, params)
            con.commit()
            return cur.fetchall()
    

    def checked(self, e):
        # Marca/desmarca uma tarefa como completa/incompleta no banco
        is_checked = e.control.value
        label = e.control.label

        if is_checked:
            self.db_execute('UPDATE tasks SET status = "complete" WHERE name = ?', params=[label])
        else:
            self.db_execute('UPDATE tasks SET status = "incomplete" WHERE name = ?', params=[label])
        
        if self.view =='all':
            self.results = self.db_execute('SELECT * FROM tasks')
        else:
            self.results = self.db_execute('SELECT * FROM tasks WHERE status = ?', params=[self.view])

        self.refresh_tasks()


    def delete_task(self, e):
        # Exclui uma tarefa do banco e atualiza a UI
        task_name = e.control.data
        self.db_execute("DELETE FROM tasks WHERE name = ?", [task_name])
        self.refresh_tasks()


    def refresh_tasks(self):
        # Atualiza a lista de tarefas com base na aba selecionada
        if self.view == "all":
            self.results = self.db_execute("SELECT * FROM tasks")
        else:
            self.results = self.db_execute("SELECT * FROM tasks WHERE status = ?", [self.view])

        self.update_task_list()
   

    def tasks_container(self):
        # Cria o contêiner que exibe as tarefas
        return ft.Container(
            height=self.page.height * 0.8,
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Checkbox(
                                label=res[0],
                                on_change=self.checked,
                                value=True if res[1] == 'complete' else False
                            ),
                            ft.IconButton(
                                icon=ft.Icons.DELETE,
                                icon_color=ft.Colors.RED,
                                tooltip="Excluir tarefa",
                                on_click=self.delete_task,
                                data=res[0],
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ) for res in self.results if res
                ]
            )
        )
    

    def set_value(self, e):
        self.task = e.control.value
    

    def add(self, e, input_task):
        # Adiciona uma nova tarefa
        name = self.task.strip()
        if name:
            self.db_execute("INSERT INTO tasks VALUES(?, ?)", [name, "incomplete"])
            input_task.value = ""
            self.task = ""  # Reseta a variável para evitar duplicações
            self.refresh_tasks()
    

    def update_task_list(self):
        # Atualiza a UI com a nova lista de tarefas
        self.page.controls.pop()
        self.page.add(self.tasks_container())
        self.page.update()


    def tabs_changed(self, e):
        """Filtra as tarefas conforme a aba selecionada"""
        tab_index = e.control.selected_index
        if tab_index == 0:
            self.view = "all"
        elif tab_index == 1:
            self.view = "incomplete"
        elif tab_index == 2:
            self.view = "complete"

        self.refresh_tasks()


    def main_page(self):
        # Configura a interface principal
        input_task = ft.TextField(
            hint_text='Digite aqui uma tarefa',
            border_color=ft.Colors.WHITE,
            expand=True,
            on_change=self.set_value
        )

        input_bar = ft.Row(
            controls=[   
                input_task,
                ft.FloatingActionButton(
                    icon=ft.Icons.ADD,
                    on_click=lambda e: self.add(e, input_task),
                ),
            ]
        )

        tabs = ft.Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[
                ft.Tab(text='ToDos'),
                ft.Tab(text='Em andamento'),
                ft.Tab(text='Finalizados'),
            ]
        )

        tasks = self.tasks_container()

        self.page.add(input_bar, tabs, tasks)


ft.app(target=ToDo)

# flet pack todo.py