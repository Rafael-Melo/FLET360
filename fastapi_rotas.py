import flet as ft
import flet_fastapi

app = flet_fastapi.FastAPI()

async def counter(page: ft.Page):
    counter = ft.Text('0', size=50, data=0)

    async def add_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        await counter.update_async()
    
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD, on_click=add_click
    )

    await page.add_async(
        ft.Container(counter, alignment=ft.alignment.center, expand=True),
    )

async def root_main(page: ft.Page):
    await page.add_async(ft.Text('Página inicial'))

async def sub_main(page: ft.Page):
    await page.add_async(ft.Text('Página secundária com outro app sendo executado'))

app.mount(path='/', app=flet_fastapi.app(root_main))
app.mount(path='/sub-app', app=flet_fastapi.app(sub_main))
app.mount(path='/counter', app=flet_fastapi.app(counter))

# pip install flet-fastapi
# pip instal uvicorn

# uvicorn aula:app --reload