import flet as ft
import datetime

def main(page: ft.Page):
    dp = ft.DatePicker(
        cancel_text='Cancelar',
        confirm_text='Confirmar',
        error_format_text='Data inválida',
        field_hint_text='MM/DD/YYYY',
        field_label_text='Digite uma data',
        help_text='Data',
        switch_to_calendar_icon=ft.icons.CALENDAR_MONTH,
        switch_to_input_icon=ft.icons.EDIT,

        date_picker_mode=ft.DatePickerMode.DAY,
        date_picker_entry_mode=ft.DatePickerEntryMode.CALENDAR,
        value=datetime.date(2025, 2, 10),
        first_date=datetime.date(2025, 1, 2),
        last_date=datetime.date(2025, 12, 31),
        error_invalid_text='Data fora do limite',

        keyboard_type=ft.KeyboardType.NUMBER,

        on_change=lambda _: print(dp.value),
    )

    page.overlay.append(dp)
    
    btn = ft.ElevatedButton('Abrir', on_click=lambda _: dp.pick_date())

    page.add(btn)


if __name__ == '__main__':
    ft.app(target=main)
