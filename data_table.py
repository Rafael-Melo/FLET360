import flet as ft

def main(page: ft.Page):
    def toggle_selected(e):
        e.control.selected = not e.control.selected
        print(f'Selecionando a linha de índice {e.control.data}')
        dt.update()


    def sort_table(e):
        dt.rows.sort(key=lambda row: row.cells[e.column_index].content.value, reverse=not e.ascending)
        dt.update()

        
    dt = ft.DataTable(
        columns=[
            ft.DataColumn(
                label=ft.Text('Nome'),
                on_sort=sort_table,
                ),
            ft.DataColumn(
                label=ft.Text('Login'),
                tooltip='Login do usuário na plataforma',
                on_sort=sort_table,
                ),
            ft.DataColumn(
                label=ft.Text('Idade'),
                numeric=True,
                on_sort=sort_table,
                ),
            ft.DataColumn(
                label=ft.Text('Obs'),
                on_sort=sort_table,
                ),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(
                        content=ft.Text('Aline'),
                        show_edit_icon=True,
                        on_tap=lambda e: print(f"Célula: Nome - {e.control.content.value}"),
                    ),
                    ft.DataCell(content=ft.Text('alininha89')),
                    ft.DataCell(content=ft.Text('35')),
                    ft.DataCell(content=ft.Text('TESTE')),
                ],
                selected=True,
                on_select_changed=toggle_selected,
                data =0,
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(content=ft.Text('Rafael'),
                    show_edit_icon=True,
                    on_tap=lambda e: print(f"Célula: Nome - {e.control.content.value}"),
                    ),
                    ft.DataCell(content=ft.Text('rafinha88')),
                    ft.DataCell(content=ft.Text('36')),
                    ft.DataCell(content=ft.Text('OI')),
                ],
                selected=False,
                on_select_changed=toggle_selected,
                data =1,
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(content=ft.Text('Samara'),
                    show_edit_icon=True,
                    on_tap=lambda e: print(f"Célula: Nome - {e.control.content.value}"),
                    ),
                    ft.DataCell(content=ft.Text('sammy10')),
                    ft.DataCell(content=ft.Text('14')),
                    ft.DataCell(content=ft.Text('TESTE')),
                ],
                selected=False,
                on_select_changed=toggle_selected,
                data =2,
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(content=ft.Text('Nicole'),
                    show_edit_icon=True,
                    on_tap=lambda e: print(f"Célula: Nome - {e.control.content.value}"),
                    ),
                    ft.DataCell(content=ft.Text('nick22')),
                    ft.DataCell(content=ft.Text('3')),
                    ft.DataCell(content=ft.Text('TESTE')),
                ],
                selected=False,
                on_select_changed=toggle_selected,
                data =3,
            ),
        ],
        show_checkbox_column=True, # Só funciona se tiver a função on_select_changed
        bgcolor=ft.Colors.GREY_900,
        border=ft.border.all(width=2, color=ft.Colors.BLACK),
        border_radius=ft.border_radius.all(5),
        column_spacing=100,
        data_row_min_height=10,
        data_row_max_height=50,
        data_text_style=ft.TextStyle(italic=True),
        # divider_thickness=5,
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
            colors=[ft.Colors.TEAL, ft.Colors.CYAN]
        ),
        data_row_color={
            ft.MaterialState.SELECTED: ft.Colors.RED,
            ft.MaterialState.DEFAULT: ft.Colors.GREEN_700,
        },
        heading_row_color=ft.Colors.BLACK,
        heading_row_height=65,
        heading_text_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
        horizontal_lines=ft.BorderSide(width=5, color=ft.Colors.AMBER),
        vertical_lines=ft.BorderSide(width=5, color=ft.Colors.AMBER),
        horizontal_margin=25,
        show_bottom_border=True,
        # sort_column_index=0,
        sort_ascending=True,
    )

    page.add(dt)


if __name__ == '__main__':
    ft.app(target=main)