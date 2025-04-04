import flet as ft

def main(page: ft.Page):
    page.title='Music Player'
    
    def volume_down(e):
        audio.volume -= 0.05
        t.value = 'Volume: ' + str(audio.volume)
        page.update()
    

    def volume_up(e):
        audio.volume += 0.05
        t.value = 'Volume: ' + str(audio.volume)
        page.update()


    def balance_left(e):
        audio.balance -= 0.1
        audio.update()


    def balance_right(e):
        audio.balance += 0.1
        audio.update()


    audio = ft.Audio(
        src='/audio/Linkin Park The Emptiness Machine.mp3',
        autoplay=False,
        balance=0,
        volume=0.05,
        on_loaded=lambda _: print('Carregado'),
        on_duration_changed=lambda e: print('Duração:', e.data),
        on_position_changed=lambda e: print('Posição:', e.data),
        on_state_changed=lambda e: print('Estado:', e.data),
        on_seek_complete=lambda e: print('Completo:', e.data),
    )

    page.overlay.append(audio)

    t = ft.Text(value='Volume: ' + str(audio.volume))

    page.add(
        ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.PLAY_CIRCLE, on_click=lambda _: audio.play()),
                ft.IconButton(icon=ft.icons.PAUSE_CIRCLE, on_click=lambda _: audio.pause()),
                ft.IconButton(icon=ft.icons.PLAY_ARROW, on_click=lambda _: audio.resume()),
                ft.IconButton(icon=ft.icons.FORWARD_10, on_click=lambda _: audio.seek(audio.get_current_position() + 10000)),
                ft.IconButton(icon=ft.icons.REPLAY_10, on_click=lambda _: audio.seek(audio.get_current_position() - 10000)),
            ]
        ),
        ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.VOLUME_DOWN, on_click=volume_down),
                ft.IconButton(icon=ft.icons.VOLUME_UP, on_click=volume_up),
                ft.IconButton(icon=ft.icons.EXPOSURE_MINUS_1, on_click=balance_left),
                ft.IconButton(icon=ft.icons.EXPOSURE_PLUS_1, on_click=balance_right),
            ]
        ),
        t
    )


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')